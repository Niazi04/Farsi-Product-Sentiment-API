import joblib
from flask import current_app
from time import sleep
from pathlib import Path

def loadModelWithRetry() -> bool:

    if current_app.config['MODEL_READY']: return True

    BASE_PATH  = Path(__file__).resolve().parents[2]
    MODEL_PATH = BASE_PATH / "model"

    for attempt in range(1, current_app.config['MAX_LOAD_ATTEMPT'] +1):
        try:
            current_app.config['vectorizer']   = joblib.load(MODEL_PATH / "vectorizer.pkl")
            current_app.config['svm']          = joblib.load(MODEL_PATH / "svm_model.pkl")
            current_app.config['MODEL_READY']  = True

            return True

        except Exception as e:
            print("Error Happened While Loading Sentiment Model")
            if attempt <= current_app.config['MAX_LOAD_ATTEMPT']:  sleep(2)

    return False