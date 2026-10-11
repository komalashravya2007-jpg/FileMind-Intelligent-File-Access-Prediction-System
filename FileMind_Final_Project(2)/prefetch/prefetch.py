import os
import shutil

BASE = os.path.dirname(os.path.dirname(__file__))
CACHE = os.path.join(BASE, "prefetch", "cache")
os.makedirs(CACHE, exist_ok=True)

def prefetch(file_path):
    if not file_path or not os.path.exists(file_path):
        print("Prefetch skipped: file not found.")
        return None

    destination = os.path.join(CACHE, os.path.basename(file_path))
    shutil.copy2(file_path, destination)
    print("Prefetched:", destination)
    return destination

def cached_path(file_name):
    path = os.path.join(CACHE, os.path.basename(file_name))
    return path if os.path.exists(path) else None
