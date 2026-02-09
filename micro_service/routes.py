from flask import Blueprint, jsonify, request, current_app
from micro_service.utils.decorators import modelRequired

sentimentApp = Blueprint('sentiment', __name__)

@sentimentApp.route("/predict", methods=["POST"])
@modelRequired
def predictReview():
    data = request.get_json()
    if not data:
        return  jsonify({
            "error": "body is not complete - check the documentation",
            "success": False
        }), 400

    review = data.get("review", "")
    print(review)
    if not review or not review.strip():
        return jsonify({
            "error": "No review to analyze - chech the documentation",
            "success": False
        }), 400
    
    reviewVEC = current_app.config['vectorizer'].transform([review])
    polarity  = current_app.config['svm'].predict(reviewVEC)

    response = {
        "polarity": polarity[0],
        "success": True
    }

    return jsonify(response), 200