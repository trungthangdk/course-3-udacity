import os
from flask import Flask, request, jsonify
from flask.logging import create_logger
import logging

import pandas as pd
import joblib
from sklearn.preprocessing import StandardScaler

app = Flask(__name__)
LOG = create_logger(app)
LOG.setLevel(logging.INFO)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def scale(payload):
    """Scales Payload"""

    LOG.info("Scaling Payload: %s", payload)  # Corrected logging format
    scaler = StandardScaler().fit(payload)
    scaled_adhoc_predict = scaler.transform(payload)
    return scaled_adhoc_predict

@app.route("/")
def home():
    html = "<h3>Sklearn Prediction Home</h3>"
    return html

# Log out the prediction value
@app.route("/predict", methods=['POST'])
def predict():
    # Performs an sklearn prediction
    try:
        model_path = os.path.join(BASE_DIR, "Housing_price_model", "LinearRegression.joblib")
        # Load pretrained model as clf. Try any one model.
        clf = joblib.load(model_path)
        # clf = joblib.load("./Housing_price_model/StochasticGradientDescent.joblib")
        # clf = joblib.load("./Housing_price_model/GradientBoostingRegressor.joblib")
    except FileNotFoundError:
        LOG.error("Model file not found. Please check the file path.")
        return "Model file not found", 500
    except Exception as e:  # Catch specific exception
        LOG.error("Error loading model: %s", str(e))  # Log error with exception message
        return "Model not loaded", 500  # Return HTTP 500 status code for server error

    json_payload = request.json
    LOG.info("JSON payload: %s", json_payload)  # Corrected logging format
    inference_payload = pd.DataFrame(json_payload)
    LOG.info("Inference payload DataFrame: %s", inference_payload)  # Corrected logging format
    scaled_payload = scale(inference_payload)
    prediction = list(clf.predict(scaled_payload))
    LOG.info("Prediction: %s", prediction)  # Added log for prediction value
    return jsonify({'prediction': prediction})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
