import os
import socket

from flask import Flask, jsonify
from prometheus_client import CONTENT_TYPE_LATEST, Counter, generate_latest

app = Flask(__name__)

REQUESTS = Counter("app_requests_total", "Total HTTP requests", ["endpoint"])
VERSION = os.getenv("APP_VERSION", "dev")


@app.get("/")
def index():
    REQUESTS.labels(endpoint="/").inc()
    return jsonify(
        message="Hello from my CD pipeline! 🚀",
        version=VERSION,
        host=socket.gethostname(),
    )


@app.get("/health")
def health():
    return jsonify(status="ok")


@app.get("/metrics")
def metrics():
    return generate_latest(), 200, {"Content-Type": CONTENT_TYPE_LATEST}
