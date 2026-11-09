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

Requer Docker instalado (ou um GitHub Codespace, que já traz o Docker). Execute os comandos na raiz do projeto, onde está o `Dockerfile`.

```bash
# 1. construir a imagem
docker build -t opstrack-api:0.1.0 .

# 2. subir o container em segundo plano, publicando a porta 8000
docker run -d --name opstrack -p 8000:8000 opstrack-api:0.1.0

# 3. testar
curl localhost:8000/status
```

A API responde em `http://localhost:8000`. No container ela roda com o gunicorn, e não com o servidor de desenvolvimento do Flask (que usa a porta 5000).

### Comandos úteis

```bash
docker ps                  # o container deve aparecer como (healthy)
docker logs opstrack       # logs do gunicorn
docker stop opstrack       # parar o container
docker rm opstrack         # remover o container parado
docker rm -f opstrack      # parar e remover de uma vez
```

### Problemas comuns

- `port is already allocated`: a porta 8000 está em uso. Use `-p 8001:8000` e acesse `http://localhost:8001`.
- `name already in use`: já existe um container chamado `opstrack`. Rode `docker rm -f opstrack` e suba de novo.
- Container `unhealthy`: rode `docker logs opstrack` e confira a porta e o alvo do gunicorn (`app:app`).
