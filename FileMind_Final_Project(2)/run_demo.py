import os, sys

BASE = os.path.dirname(__file__)
sys.path.insert(0, os.path.join(BASE, "prediction"))

from predictor import train, predict

train()
for current in ["notes.txt", "python.py", "image.png"]:
    nxt, confidence = predict(current)
    print(f"\nCurrent file: {current}")
    print(f"Predicted next: {nxt}")
    print(f"Confidence: {confidence*100:.1f}%")
