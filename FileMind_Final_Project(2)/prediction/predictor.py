import csv
import os
import pickle
from collections import defaultdict, Counter

BASE = os.path.dirname(os.path.dirname(__file__))
HISTORY_FILE = os.path.join(BASE, "data", "access_history.csv")
MODEL_FILE = os.path.join(BASE, "models", "model.pkl")

def load_history():
    if not os.path.exists(HISTORY_FILE):
        return []
    with open(HISTORY_FILE, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))

def train():
    rows = load_history()
    transitions = defaultdict(Counter)

    previous = None
    for row in rows:
        current = row["file_name"]
        if previous and previous != current:
            transitions[previous][current] += 1
        previous = current

    model = dict(transitions)
    os.makedirs(os.path.dirname(MODEL_FILE), exist_ok=True)
    with open(MODEL_FILE, "wb") as f:
        pickle.dump(model, f)

    print(f"Training complete. Records: {len(rows)}")
    print(f"Learned transitions: {sum(len(v) for v in model.values())}")
    return model

def predict(current_file):
    if not os.path.exists(MODEL_FILE):
        train()
    with open(MODEL_FILE, "rb") as f:
        model = pickle.load(f)

    choices = model.get(os.path.basename(current_file), {})
    if not choices:
        return None, 0.0

    total = sum(choices.values())
    next_file, count = choices.most_common(1)[0]
    confidence = count / total if total else 0.0
    return next_file, confidence

if __name__ == "__main__":
    import sys
    model = train()
    if len(sys.argv) > 1:
        result, confidence = predict(sys.argv[1])
        print("Predicted next file:", result)
        print("Confidence:", round(confidence * 100, 2), "%")
