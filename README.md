# 💰 Cashback API

API para cálculo de cashback com frontend estático, feita com **FastAPI** + **PostgreSQL**.

## Regras de Negócio

- Cashback base: **5%** sobre o valor final (após descontos)
- Clientes **VIP**: bônus de **+10%** sobre o cashback base
- Compras acima de **R$ 500** (valor final): cashback **dobrado**
- Ordem: base → bônus VIP → promoção

## Estrutura

```
app/
├── main.py              # Entrada da aplicação
├── database.py          # Conexão com o banco
├── models/
│   └── consulta.py      # Tabela do banco
├── schemas/
│   └── dados_compra.py  # Validação de entrada
├── services/
│   └── cashback_service.py  # Cálculo do cashback
└── controllers/
    └── cashback_controller.py  # Rotas da API
static/
├── index.html           # Frontend
├── style.css            # Estilos
└── app.js               # JavaScript
```

## Endpoints

| Método | Rota             | Descrição                         |
|--------|------------------|-----------------------------------|
| GET    | `/`              | Frontend (calculadora)            |
| POST   | `/api/calcular`  | Calcula cashback e salva no banco |
| GET    | `/api/historico` | Histórico de consultas por IP     |

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

### Sem Docker

Precisa ter PostgreSQL rodando na porta 5432.

```bash
docker compose up -d db

python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

uvicorn app.main:app --reload
```

Acesse: **http://localhost:8000**

## Tecnologias

- **Backend:** Python, FastAPI, SQLAlchemy, Databases
- **Banco:** PostgreSQL
- **Frontend:** HTML, CSS, JavaScript puro
- **Infra:** Docker, Docker Compose
