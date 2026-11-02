Construction Intelligence — AI-Powered Project Estimation & Analytics
An end-to-end Python application for analysing construction project data, monitoring project performance, and estimating labour and material requirements for future projects. It combines a reproducible data pipeline, SQL-based reporting, machine learning, and an interactive web dashboard.
Data notice: The sample dataset is entirely synthetic. This application is a demonstration prototype and its estimates should not be used for operational or financial decisions without validation on representative real-world data.

Features
- Data ingestion and validation: Load simulated construction project records from CSV into an indexed SQLite reporting database.
- Business intelligence: Explore project costs, budget variance, category-level summaries, KPIs, and interactive Plotly visualisations.
- Predictive estimation: Train a scikit-learn multi-output Random Forest to estimate labour hours and material quantities from early project characteristics.
- Interactive application: Use a Streamlit dashboard to review performance, generate project estimates, adjust costing assumptions, and export results to CSV.
- Reproducibility and quality: Regenerate sample data and model artefacts, run automated tests, and use the included GitHub Actions workflow.
Technology stack
Python · pandas · scikit-learn · SQLite · SQL · Streamlit · Plotly · pytest · GitHub Actions
Getting started
Requirements
- Python 3.11 or 3.12
- Visual Studio Code (recommended) with the Python extension, or another Python development environment
Windows (PowerShell)
Open the project folder in VS Code, then run the following commands in its terminal:
py -3.11 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python -m scripts.bootstrap
streamlit run app.py
If Python 3.11 is not available through the py launcher, use python -m venv .venv. If PowerShell prevents environment activation, run commands with .venv\Scripts\python.exe instead of python and .venv\Scripts\streamlit.exe instead of streamlit.
macOS / Linux
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python -m scripts.bootstrap
streamlit run app.py
Open http://localhost:8501 to use the application.
Typical workflow
1. Prepare data: Run python -m scripts.bootstrap to generate synthetic project records, populate the SQLite database, and train the estimation model.
2. Explore performance: Open the Streamlit dashboard to review project KPIs, budgets, costs, and visualisations.
3. Estimate a project: Enter project type, area, complexity, and planned duration; generate predicted labour hours and material quantities.
4. Review indicative costs: Adjust labour and material rates to calculate scenario-based estimates.
5. Export results: Download relevant data or estimates as CSV for further analysis.
Architecture
Synthetic project data (CSV)
          |
          v
Validation and ETL pipeline
          |
          v
SQLite reporting database ---> SQL KPI views ---> Streamlit dashboard
          |
          v
Model training and evaluation
          |
          v
Trained estimation model ---> Project estimator ---> CSV export
See [architecture.md](architecture.md) for additional technical details. The current implementation uses SQLite and Streamlit. Connections to external enterprise systems or BI platforms are possible future extensions; they are not included in this prototype.
Machine learning approach
- Inputs: Project type, project area, complexity, and planned duration.
- Targets: Labour hours and material units.
- Algorithm: Multi-output Random Forest regression.
- Evaluation: Chronological 80/20 holdout with MAE, RMSE, and R² reported separately for each target.
- Leakage safeguards: Budget, actual cost, costing rates, and target quantities are excluded from predictive model inputs. Rates are applied after prediction to calculate indicative costs.
Limitations: The dataset is simulated, so evaluation metrics do not establish performance on actual construction projects. The single chronological split is illustrative rather than a comprehensive backtesting procedure. Before real-world use, the system would need data-quality checks, additional validation, model monitoring, access controls, and governed cost assumptions.
Run automated tests
python -m pytest -q
Publish to GitHub
Create an empty GitHub repository, for example construction-intelligence-platform, and run:
git init
git add .
git commit -m "Initial construction intelligence platform"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/construction-intelligence-platform.git
git push -u origin main
Replace YOUR_USERNAME with your GitHub username. Generated databases and trained model artefacts are excluded from version control and can be recreated with python -m scripts.bootstrap.
Future enhancements
- Connect to production data sources using authenticated APIs and scheduled ingestion.
- Add configurable reporting dimensions and operational KPI definitions.
- Compare multiple regression models and apply rolling-origin validation.
- Include uncertainty intervals, model monitoring, and drift detection.
- Add role-based access controls and deployment configuration.
Data and usage disclaimer
All included project records are fictional and are intended for development, testing, and demonstration. Predicted quantities and costs are illustrative, not professional construction estimates.
