import sqlalchemy
from datetime import datetime
from app.database import metadata

cashback = sqlalchemy.Table(
    "cashback",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("ip", sqlalchemy.String(45), nullable=False, index=True),
    sqlalchemy.Column("tipo_cliente", sqlalchemy.String(10), nullable=False),
    sqlalchemy.Column("valor_compra", sqlalchemy.Float, nullable=False),
    sqlalchemy.Column("desconto", sqlalchemy.Float, nullable=False),
    sqlalchemy.Column("valor_final", sqlalchemy.Float, nullable=False),
    sqlalchemy.Column("cashback", sqlalchemy.Float, nullable=False),
    sqlalchemy.Column("criacao", sqlalchemy.DateTime, default=datetime.utcnow),
)
