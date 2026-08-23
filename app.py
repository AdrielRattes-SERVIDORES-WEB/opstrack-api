from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return {"status": "ok", "service": "opstrack-api"}


@app.route("/status")
def status():
    return {"status": "operational"}


if __name__ == "__main__":
    app.run(debug=True)
