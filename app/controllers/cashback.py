from fastapi import APIRouter, Request
from datetime import datetime

from app.database import database
from app.models.consulta import consultas
from app.schemas.consulta import ConsultaRequest
from app.services.cashback import calcular_cashback
from app.utils.request import get_client_ip

router = APIRouter(prefix="/api")


@router.post("/calcular")
async def calcular(request: Request, body: ConsultaRequest):
    ip = get_client_ip(request)
    resultado = calcular_cashback(body.valor_compra, body.desconto, body.tipo_cliente)

    query = consultas.insert().values(
        ip=ip,
        tipo_cliente=body.tipo_cliente.upper(),
        valor_compra=body.valor_compra,
        desconto=body.desconto,
        valor_final=resultado["valor_final"],
        cashback=resultado["cashback_final"],
        criado_em=datetime.utcnow(),
    )
    await database.execute(query)

    return {**resultado, "ip": ip}


@router.get("/historico")
async def historico(request: Request):
    ip = get_client_ip(request)
    query = (
        consultas.select()
        .where(consultas.c.ip == ip)
        .order_by(consultas.c.criado_em.desc())
        .limit(50)
    )
    rows = await database.fetch_all(query)
    return [
        {
            "id": r["id"],
            "tipo_cliente": r["tipo_cliente"],
            "valor_compra": r["valor_compra"],
            "desconto": r["desconto"],
            "valor_final": r["valor_final"],
            "cashback": r["cashback"],
            "criado_em": r["criado_em"].isoformat(),
        }
        for r in rows
    ]
