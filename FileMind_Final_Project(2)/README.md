# FileMind — Intelligent File Access Prediction System

## Objective
FileMind monitors file-access activity, stores historical access patterns, predicts the next likely file, and prepares the predicted file for faster retrieval.

## Pipeline
Monitor → Record → Analyse → Predict → Prefetch → Access

## Project structure
- `monitor/` — file activity monitoring
- `data/` — access history
- `prediction/` — next-file prediction
- `prefetch/` — predicted-file cache
- `dashboard/` — Streamlit dashboard
- `models/` — saved prediction model
- `results/` — experimental results

## Run on Windows
1. Install Python 3.11+.
2. Open terminal in this folder.
3. Run:
   `python -m pip install -r requirements.txt`
4. Generate demo history:
   `python generate_demo_data.py`
5. Train and test:
   `python run_demo.py`
6. Start dashboard:
   `streamlit run dashboard/app.py`

## Linux extension
For the final Linux/OS demonstration, the monitoring layer can be connected to Linux file-event mechanisms/system calls. The prediction and dashboard layers remain unchanged.

## Important
The included demo uses synthetic access-history data so the project can be demonstrated immediately. It does not claim kernel-level monitoring or a measured speed improvement until those are experimentally implemented and measured.
