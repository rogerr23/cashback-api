import sqlalchemy
from datetime import datetime
from app.database import metadata

consultas = sqlalchemy.Table(
    "consultas",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("ip", sqlalchemy.String(45), nullable=False, index=True),
    sqlalchemy.Column("tipo_cliente", sqlalchemy.String(10), nullable=False),
    sqlalchemy.Column("valor_compra", sqlalchemy.Float, nullable=False),
    sqlalchemy.Column("desconto", sqlalchemy.Float, nullable=False),
    sqlalchemy.Column("valor_final", sqlalchemy.Float, nullable=False),
    sqlalchemy.Column("cashback", sqlalchemy.Float, nullable=False),
    sqlalchemy.Column("criado_em", sqlalchemy.DateTime, default=datetime.utcnow),
)
