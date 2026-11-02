# Construction Intelligence — Data & AI Engineer KTP Portfolio

An **end-to-end runnable portfolio project** aligned with the Ulster University / Michael Nugent Ltd **Data and AI Engineer (KTP Associate)** briefing, reference 044106. This is an independent demonstration, **not** an official Nugent system.

## What it demonstrates

- **ETL and data modelling:** fictional construction jobs CSV → validation → indexed SQLite reporting table and KPI SQL view.
- **SQL and BI:** project costs, budget variance, category totals, executive metrics and interactive Plotly charts.
- **Predictive AI:** scikit-learn multi-output Random Forest predicting labour hours and material quantities from early project characteristics.
- **Usable interface:** Streamlit estimator, editable costing assumptions, CSV exports and model evaluation panel.
- **Engineering:** reproducible synthetic data, unit tests, GitHub Actions CI, architecture documentation.

## Quick start in Visual Studio Code

Prerequisites: Python 3.11 or 3.12, VS Code, Python extension.

```powershell
# In VS Code Terminal (Windows PowerShell)
py -3.11 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python -m scripts.bootstrap
streamlit run app.py
```

If `py -3.11` is not installed, use `python -m venv .venv`. On macOS/Linux, activate with `source .venv/bin/activate`. If PowerShell blocks activation, use `.venv\Scripts\python.exe -m pip install -r requirements.txt` and similarly prefix other Python commands, or switch the VS Code terminal to Command Prompt.

Streamlit opens at `http://localhost:8501`.

## Run tests

```bash
python -m pytest -q
```

## Upload to GitHub

Create an empty GitHub repository (for example `construction-intelligence-ktp`), then in VS Code terminal:

```bash
git init
git add .
git commit -m "Initial end-to-end construction intelligence demo"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/construction-intelligence-ktp.git
git push -u origin main
```

Replace `YOUR_USERNAME` with your own GitHub username. Generated database and trained models are ignored; every clone recreates them with `python -m scripts.bootstrap`.

## Architecture

See [architecture.md](architecture.md). Current demo uses SQLite and Streamlit; **Power BI and Microsoft Dynamics 365 Business Central are proposed integration targets, not implemented integrations**.

## Model design and limitations

- Inputs: project type, area, complexity and planned duration. Rates are used **only after prediction** for cost calculation.
- Targets: labour hours and material units.
- Evaluation: 80/20 chronological holdout, MAE/RMSE/R² on both targets.
- Budget, actual cost, material rate, labour rate, and target quantities are **not model inputs**, avoiding direct target leakage.
- Data is simulated, so performance is not evidence of effectiveness on real company projects. Real deployment needs real data validation, drift monitoring, access controls, approvals and cost-rate governance.
- The date split is a simple demonstration, not a complete time-aware backtesting strategy.

## Interview demonstration (5 minutes)

1. **0:00–0:45:** Explain business problem: disconnected data, inconsistent reporting and manual estimates.
2. **0:45–1:30:** Show architecture and CSV-to-SQLite pipeline.
3. **1:30–2:20:** Show executive dashboard and project KPIs.
4. **2:20–3:40:** Enter a new project and generate labour/material estimate with cost assumptions.
5. **3:40–5:00:** Show evaluation, discuss leakage safeguards and how you would connect Business Central and Power BI in production.

## Portfolio ethics

All records are fictional. This project is not affiliated with or endorsed by Michael Nugent Ltd or Ulster University. Do not present simulated results as real operational outcomes.
