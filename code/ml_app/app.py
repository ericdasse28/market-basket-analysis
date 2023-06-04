"""Article recommendation API"""

import os
from pathlib import Path
from flask import Flask, jsonify, request
import joblib


app = Flask(__name__)


@app.route("/recommend_next_product", methods=["POST"])
def recommend():
    json = request.get_json()
    product = json["product"]

    # Loading saved model
    repo_path = Path(__file__).parent.parent.parent
    model_path = os.environ.get("MODEL_PATH", repo_path / "model/association_rules.pkl")
    model_df = joblib.load(model_path)
    # Perform next product prediction here
    prediction_info = model_df[model_df["Product1"] == product]
    predicted_product = prediction_info["Product2"][0]
    confidence = prediction_info["Confidence (%)"][0]

    res = {"next_product": predicted_product, "confidence": confidence}
    return jsonify(res)


if __name__ == "__main__":
    app.run(host="0.0.0.0")
