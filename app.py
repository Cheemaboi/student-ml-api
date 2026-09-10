from flask import Flask, jsonify, request


app = Flask(__name__)


def current_version() -> str:
    with open("VERSION", encoding="utf-8") as version_file:
        return version_file.read().strip()


@app.get("/health")
def health():
    return jsonify(
        status="healthy",
        application="student-ml-api",
        application_version=current_version(),
        model_version="model-1",
    )


@app.post("/predict")
def predict():
    payload = request.get_json(silent=True)
    if not isinstance(payload, dict) or "value" not in payload:
        return jsonify(error="'value' is required"), 400

    value = payload["value"]
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        return jsonify(error="'value' must be numeric"), 400

    return jsonify(input=value, prediction=value * 2)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
