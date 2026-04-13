def calcular_cashback(valor_compra: float, desconto: float, tipo_cliente: str) -> dict:
    """Aplica as regras de negócio do cashback."""
    valor_final = valor_compra * (1 - desconto)
    cashback_base = valor_final * 0.05

    cashback_com_bonus = (
        cashback_base * 1.10 if tipo_cliente.upper() == "VIP" else cashback_base
    )

    cashback_final = (
        cashback_com_bonus * 2 if valor_final > 500 else cashback_com_bonus
    )

    return {
        "valor_final": round(valor_final, 2),
        "cashback_base": round(cashback_base, 2),
        "cashback_com_bonus": round(cashback_com_bonus, 2),
        "cashback_final": round(cashback_final, 2),
        "promocao_aplicada": valor_final > 500,
        "bonus_vip_aplicado": tipo_cliente.upper() == "VIP",
    }
