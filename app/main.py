from flask import Flask, jsonify
import os

app = Flask(__name__)

ENVIRONMENT = os.getenv("ENVIRONMENT", "local")
VERSION = os.getenv("VERSION", "2.0.0")

@app.route("/")
def hello():
    return jsonify({
        "message": f"Hello from {ENVIRONMENT}",
        "version": VERSION
    })

@app.route("/health")
def health():
    return jsonify({"status": "healthy"}), 200

@app.route("/version")
def version():
    return jsonify({"version": VERSION}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
