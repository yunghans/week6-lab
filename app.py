from flask import Flask, jsonify, request

from duckfine import DuckFine


app = Flask(__name__)


@app.get("/health")
def health():
    return jsonify(status="ok")


@app.get("/fine")
def fine():
    try:
        days = int(request.args.get("days", ""))
    except ValueError:
        return jsonify(error="days must be a non-negative integer"), 400

    if days < 0:
        return jsonify(error="days must be a non-negative integer"), 400

    fee = DuckFine("online").charge(
        days, deluxe=request.args.get("deluxe") == "1"
    )
    return jsonify(fee=fee)