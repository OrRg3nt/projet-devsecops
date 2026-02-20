
from flask import Flask, jsonify, request
import os

app = Flask(__name__)

@app.route("/api/data", methods=["GET"])
def get_data():
    key = request.args.get("key", "none")
    print(f"[INFO] Request received with key={key}")
    return jsonify({"data": f"value for {key}"})

if __name__ == "__main__":
	app.run(host="0.0.0.0", port=5001111, threaded=True)
