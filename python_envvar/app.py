import os
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    app_name = os.getenv("APP_NAME")
    environment = os.getenv("ENVIRONMENT")
    version = os.getenv("APP_VERSION")

    return f"""
    <h1>{app_name}</h1>
    <h2>Python Environment Demo</h2>
    <p><b>Environment:</b> {environment}</p>
    <p><b>Version:</b> {version}</p>
    """

@app.route("/health")
def health():
    return {"status": "healthy"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)