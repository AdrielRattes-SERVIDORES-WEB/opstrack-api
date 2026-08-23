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
