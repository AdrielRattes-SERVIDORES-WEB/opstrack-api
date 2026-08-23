from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return {"status": "ok", "service": "opstrack-api"}


@app.route("/status")
def status():
    return {"status": "operational"}


@app.route("/tickets")
def tickets():
    return {
        "tickets": [
            {"id": 1, "titulo": "Impressora do 2º andar sem tinta", "status": "aberto"},
            {"id": 2, "titulo": "Acesso VPN não conecta", "status": "em andamento"},
            {"id": 3, "titulo": "Monitor externo não é detectado", "status": "fechado"},
        ]
    }


@app.route("/sobre")
def sobre():
    return {"nome": "OpsTrack API", "versao": "0.1.0"}


if __name__ == "__main__":
    app.run(debug=True)
