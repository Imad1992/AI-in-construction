# Proposed integration architecture (illustrative)

```mermaid
flowchart LR
 A[ERP / Business Central API] --> E[Extract and validate]
 B[Estimating spreadsheets] --> E
 C[Time sheets] --> E
 E --> D[(Staging and reporting database)]
 D --> K[KPI semantic layer]
 K --> P[Power BI / Business Central cue cards]
 D --> M[Versioned ML training]
 M --> U[Estimator UI]
```

**Implemented in this repository:** synthetic CSV ingestion, validation, SQLite reporting, a Streamlit KPI dashboard, and a predictive estimation interface.

**Future production integration:** authenticated Business Central OData/API ingestion, incremental sync and retries, orchestration, audit logs, row-level security, Power BI semantic model, Business Central extensions, model monitoring, human approval and deployment controls. No real Business Central integration is claimed here.
