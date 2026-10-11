import csv, os
from datetime import datetime, timedelta

BASE = os.path.dirname(__file__)
OUT = os.path.join(BASE, "data", "access_history.csv")
os.makedirs(os.path.dirname(OUT), exist_ok=True)

sequence = [
    "notes.txt", "python.py", "output.csv",
    "notes.txt", "python.py", "output.csv",
    "notes.txt", "python.py", "report.pdf",
    "notes.txt", "python.py", "output.csv",
    "notes.txt", "python.py", "output.csv",
    "image.png", "report.pdf", "notes.txt"
]

start = datetime.now()
with open(OUT, "w", newline="", encoding="utf-8") as f:
    w = csv.writer(f)
    w.writerow(["timestamp", "file_path", "file_name"])
    for i, name in enumerate(sequence):
        ts = (start + timedelta(seconds=i)).isoformat(timespec="seconds")
        w.writerow([ts, os.path.join("sample_files", name), name])

print("Demo history generated:", OUT)
