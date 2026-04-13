from pydantic import BaseModel, Field


class cashback_request(BaseModel):
    tipo_cliente: str = Field(..., pattern="^(VIP|NORMAL)$")
    valor_compra: float = Field(..., gt=0)
    desconto: float = Field(0.0, ge=0, le=1)
