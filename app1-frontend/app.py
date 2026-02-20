from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({"message": "Hello from Frontend!"})

@app.route("/status")
def status():
    log_level = os.getenv("LOG_LEVEL", "INFO")
    print(f"[{log_level}] Status endpoint called")
    return jsonify({"status": "ok"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, threaded=True)
