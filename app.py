from flask import Flask, request, jsonify
from micro_service.routes import sentimentApp
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

app.config['MAX_LOAD_ATTEMPT'] = 12
app.config['MODEL_READY']      = False
app.config['svm']              = None
app.config['vectorizer']       = None

app.register_blueprint(sentimentApp)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)