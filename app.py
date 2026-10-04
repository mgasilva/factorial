from math import factorial

from flask import Flask, jsonify, request


app = Flask(__name__)


@app.get("/health")
def health() -> tuple[dict[str, str], int]:
    return {"status": "ok"}, 200


@app.get("/factorial")
def get_factorial() -> tuple[dict[str, str | int], int]:
    raw_n = request.args.get("n")
    if raw_n is None:
        return {"error": "missing required query parameter 'n'"}, 400

    try:
        n = int(raw_n)
    except ValueError:
        return {"error": "'n' must be an integer"}, 400

    if n < 0:
        return {"error": "'n' must be non-negative"}, 400

    result = factorial(n)
    return jsonify({"n": n, "factorial": str(result)}), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
