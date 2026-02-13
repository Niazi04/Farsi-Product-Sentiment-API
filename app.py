from flask import Flask, request, jsonify
from micro_service.routes import sentimentApp
from flask_cors import CORS
from datetime import timezone, datetime
from pathlib import Path

app = Flask(__name__)
CORS(app)

app.config['MAX_LOAD_ATTEMPT'] = 12
app.config['MODEL_READY']      = False
app.config['svm']              = None
app.config['vectorizer']       = None

app.register_blueprint(sentimentApp)

@app.route("/health", methods=["GET"])
def health():

    SVM_EXIST        = Path("./model/svm_model.pkl").is_file()
    VECTORIZER_EXIST = Path("./model/vectorizer.pkl").is_file()

    response = {
        "model": "loaded in memory" if app.config["MODEL_READY"] else "not loaded in memory",
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "dependencies": {
            "svm"       : "available" if SVM_EXIST        else "missing",
            "vectorizer": "available" if VECTORIZER_EXIST else "missing"
        }
    }

    statusCode = 503 if not (SVM_EXIST and VECTORIZER_EXIST) else 200

    return jsonify(response), statusCode

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)