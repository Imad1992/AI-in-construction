import streamlit as st
import pandas as pd
import plotly.express as px
import joblib
from config import DB,MODEL
from src.pipeline import read_jobs,read_kpis
from src.model import estimate

st.set_page_config(page_title='Construction Intelligence',page_icon='🏗️',layout='wide')
st.title('🏗️ Construction Intelligence Platform')
st.caption('Portfolio demonstration | Synthetic data only | Not connected to Microsoft Business Central')
if not DB.exists() or not MODEL.exists():
    st.error('Run: python -m src.generate_data, python -m src.pipeline, python -m src.model')
    st.stop()

@st.cache_data
def load(): return read_jobs(),read_kpis()
df,kpis=load()
tab1,tab2,tab3,tab4=st.tabs(['Executive dashboard','AI estimator','Project explorer','Model evaluation'])
with tab1:
    a,b,c,d=st.columns(4)
    a.metric('Completed projects',len(df))
    b.metric('Actual spend',f"£{df.actual_cost.sum():,.0f}")
    c.metric('Average budget variance',f"£{(df.actual_cost-df.budget).mean():,.0f}")
    d.metric('Total labour hours',f"{df.labour_hours.sum():,.0f}")
    x,y=st.columns(2)
    with x: st.plotly_chart(px.bar(kpis,x='project_type',y='total_actual_cost',title='Spend by project type'),use_container_width=True)
    with y: st.plotly_chart(px.scatter(df,x='area_sqm',y='actual_cost',color='project_type',title='Area vs actual cost'),use_container_width=True)
    st.dataframe(kpis,use_container_width=True,hide_index=True)
with tab2:
    st.subheader('Predict labour and materials for a new job')
    with st.form('estimate'):
        a,b=st.columns(2)
        with a:
            kind=st.selectbox('Project type',sorted(df.project_type.unique()))
            area=st.number_input('Area (square metres)',min_value=150.0,max_value=15000.0,value=2500.0,step=100.0)
            complexity=st.slider('Complexity (1 low – 5 high)',1,5,3)
        with b:
            duration=st.number_input('Planned duration (weeks)',min_value=2.0,max_value=100.0,value=16.0)
            labour_rate=st.number_input('Labour rate (£/hour)',min_value=0.01,value=30.0)
            material_rate=st.number_input('Material rate (£/unit)',min_value=0.01,value=45.0)
        submitted=st.form_submit_button('Generate estimate',type='primary')
    if submitted:
        result=estimate(kind,area,complexity,duration,labour_rate,material_rate)
        a,b,c=st.columns(3)
        a.metric('Labour hours',f"{result['labour_hours']:,.0f}")
        b.metric('Material units',f"{result['material_units']:,.0f}")
        c.metric('Indicative cost',f"£{result['estimated_cost']:,.2f}")
        st.info('Model outputs are estimates from fictional data, not validated commercial quotations. Rates are user assumptions.')
        st.download_button('Download estimate CSV',pd.DataFrame([{**{'project_type':kind,'area_sqm':area,'complexity':complexity,'duration_weeks':duration},**result}]).to_csv(index=False),file_name='estimate.csv',mime='text/csv')
with tab3:
    selected=st.multiselect('Filter project types',sorted(df.project_type.unique()),default=sorted(df.project_type.unique()))
    view=df[df.project_type.isin(selected)]
    st.dataframe(view,use_container_width=True,hide_index=True)
    st.download_button('Export filtered projects',view.to_csv(index=False),file_name='projects.csv',mime='text/csv')
with tab4:
    artifact=joblib.load(MODEL)
    st.write('Chronological 80/20 holdout (sorted by start date); targets are labour hours and material units.')
    st.write(f"Training records: {artifact['training_rows']} | Test records: {artifact['test_rows']}")
    st.dataframe(pd.DataFrame(artifact['metrics']).T,use_container_width=True)
    st.warning('Synthetic data is intentionally generated with patterns. Results do not establish real-world accuracy; validate on permissioned historical jobs before deployment.')
