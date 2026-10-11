import os
import csv
import streamlit as st

BASE = os.path.dirname(os.path.dirname(__file__))
HISTORY = os.path.join(BASE, "data", "access_history.csv")

st.set_page_config(page_title="FileMind", page_icon="📁", layout="wide")
st.title("📁 FileMind")
st.subheader("Intelligent File Access Prediction System")

rows = []
if os.path.exists(HISTORY):
    with open(HISTORY, newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))

c1, c2, c3 = st.columns(3)
c1.metric("Access Records", len(rows))
c2.metric("Unique Files", len(set(r["file_name"] for r in rows)) if rows else 0)
c3.metric("Status", "Monitoring Ready")

st.divider()
st.write("### Access History")
if rows:
    st.dataframe(rows, use_container_width=True)
else:
    st.info("No access history yet. Run the monitor or generate demo data.")

st.write("### FileMind Workflow")
st.code("""User Access
   ↓
Access Monitor
   ↓
Access History
   ↓
Pattern Analysis
   ↓
Next-File Prediction
   ↓
Prefetch
   ↓
Faster Access""")
