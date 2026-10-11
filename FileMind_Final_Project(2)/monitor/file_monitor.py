import csv
import os
import time
from datetime import datetime

HISTORY_FILE = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "access_history.csv")

def ensure_history():
    os.makedirs(os.path.dirname(HISTORY_FILE), exist_ok=True)
    if not os.path.exists(HISTORY_FILE):
        with open(HISTORY_FILE, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["timestamp", "file_path", "file_name"])

def record_access(file_path):
    ensure_history()
    file_path = os.path.abspath(file_path)
    with open(HISTORY_FILE, "a", newline="", encoding="utf-8") as f:
        csv.writer(f).writerow([
            datetime.now().isoformat(timespec="seconds"),
            file_path,
            os.path.basename(file_path)
        ])

def monitor_folder(folder, interval=1):
    """Simple cross-platform demo monitor.
    It watches modification/access-like activity by detecting changes in file metadata.
    For a true Linux syscall/inotify implementation, replace this layer on Ubuntu.
    """
    folder = os.path.abspath(folder)
    print(f"Monitoring: {folder}")
    seen = {}
    while True:
        for name in os.listdir(folder):
            path = os.path.join(folder, name)
            if not os.path.isfile(path):
                continue
            try:
                stat = os.stat(path)
                signature = (stat.st_mtime_ns, stat.st_size)
                if path not in seen:
                    seen[path] = signature
                    record_access(path)
                    print("Detected:", name)
                elif seen[path] != signature:
                    seen[path] = signature
                    record_access(path)
                    print("Changed:", name)
            except OSError:
                pass
        time.sleep(interval)

if __name__ == "__main__":
    import sys
    ensure_history()
    target = sys.argv[1] if len(sys.argv) > 1 else os.path.join(os.path.dirname(os.path.dirname(__file__)), "sample_files")
    os.makedirs(target, exist_ok=True)
    monitor_folder(target)
