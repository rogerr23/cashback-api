# 💰 Cashback API

API para cálculo de cashback com frontend estático, desenvolvida com **FastAPI** + **PostgreSQL**.

## Regras de Negócio

- Cashback base: **5%** sobre o valor final (após descontos)
- Clientes **VIP**: bônus de **+10%** sobre o cashback base
- Compras acima de **R$ 500** (valor final): cashback é **dobrado**
- Ordem de cálculo: base → bônus VIP → promoção

## Arquitetura

```
app/
├── main.py              # Entrada da aplicação (FastAPI + static files)
├── database.py          # Conexão com PostgreSQL
├── models/              # Tabelas (SQLAlchemy)
├── schemas/             # Validação de entrada (Pydantic)
├── services/            # Regras de negócio
├── controllers/         # Rotas/endpoints
└── utils/               # Funções auxiliares
static/
├── index.html           # Frontend
├── style.css            # Estilos
└── app.js               # JavaScript puro
```

## Endpoints

| Método | Rota             | Descrição                          |
|--------|------------------|------------------------------------|
| GET    | `/`              | Frontend (calculadora)             |
| POST   | `/api/calcular`  | Calcula cashback e salva no banco  |
| GET    | `/api/historico` | Histórico de consultas por IP      |

**POST `/api/calcular`** — Body:
```json
{
  "tipo_cliente": "VIP",
  "valor_compra": 600,
  "desconto": 0.20
}
```

## Como Rodar

### Com Docker (recomendado)

```bash
docker compose up -d --build
```

Acesse: **http://localhost:8000**

### Sem Docker (API local)

Pré-requisito: PostgreSQL rodando na porta 5432.

```bash
# Sobe só o Postgres via Docker
docker compose up -d db

# Cria venv e instala dependências
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

# Roda a API
uvicorn app.main:app --reload
```

Acesse: **http://localhost:8000**

### Conexão com o Banco (DBeaver)

| Campo    | Valor       |
|----------|-------------|
| Host     | `localhost` |
| Port     | `5432`      |
| Database | `cashbackdb`|
| User     | `user`      |
| Password | `password`  |

## Tecnologias

- **Backend:** Python, FastAPI, SQLAlchemy, Databases (async)
- **Banco:** PostgreSQL
- **Frontend:** HTML, CSS, JavaScript puro
- **Infra:** Docker, Docker Compose
