from functools import wraps
from flask import jsonify, current_app
from micro_service.utils.modelManager import loadModelWithRetry

def modelRequired(fn):
    @wraps(fn)
    def decoratorFn(*args, **kwargs):

        if not current_app.config['MODEL_READY']:
            retry = loadModelWithRetry()
            if not retry:
                return jsonify({
                    "error": "Sentiment Analyzer is temporarily down",
                    "success": False,
                    "code": "SERVICE_UNAVAILABLE"
                }), 503

        return fn(*args, **kwargs)
    
    return decoratorFn