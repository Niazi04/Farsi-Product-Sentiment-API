import joblib
from flask import current_app
from time import sleep

def loadModelWithRetry() -> bool:

    if current_app.config['MODEL_READY']: return True

    for attempt in range(1, current_app.config['MAX_LOAD_ATTEMPT'] +1):
        try:
            current_app.config['vectorizer']   = joblib.load("./model/vectorizer.pkl")
            current_app.config['svm']          = joblib.load("./model/svm_model.pkl")
            current_app.config['MODEL_READY']  = True

            return True

        except Exception as e:
            print("Error Happened While Loading Sentiment Model")
            if attempt <= current_app.config['MAX_LOAD_ATTEMPT']:  sleep(2)

    return False