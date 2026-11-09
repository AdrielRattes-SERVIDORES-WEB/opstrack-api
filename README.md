# OpsTrack API

API simples de controle de chamados de TI (tickets), construída com Flask.

## Setup

```bash
python -m venv venv
venv\Scripts\activate        # Windows
source venv/bin/activate     # Linux/Mac
pip install -r requirements.txt
python app.py
```

A aplicação sobe em `http://127.0.0.1:5000`.

## Rotas disponíveis

| Rota | Descrição |
|---|---|
| `GET /` | Status geral do serviço |
| `GET /status` | Disponibilidade do serviço |
| `GET /tickets` | Lista mockada de chamados de TI |
| `GET /sobre` | Nome e versão da API |

## Rodando com Docker

Na raiz do projeto (onde está o `Dockerfile`):

```bash
# construir a imagem
docker build -t opstrack-api:0.1.0 .

# subir o container em segundo plano, publicando a porta 8000
docker run -d --name opstrack -p 8000:8000 opstrack-api:0.1.0

# testar
curl localhost:8000/status

# ver os logs
docker logs opstrack

# parar e remover o container
docker stop opstrack
docker rm opstrack
```

A API dentro do container usa o gunicorn e escuta na porta **8000** (diferente da 5000 do `python app.py`). Se a porta 8000 já estiver ocupada, use `-p 8001:8000`.
