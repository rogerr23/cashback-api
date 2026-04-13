const $ = (id) => document.getElementById(id);
const moeda = (v) => `R$ ${v.toFixed(2).replace(".", ",")}`;

$("form").addEventListener("submit", async (e) => {
  e.preventDefault();
  const body = {
    tipo_cliente: $("tipo").value,
    valor_compra: parseFloat($("valor").value),
    desconto: (parseFloat($("desconto").value) || 0) / 100,
  };

  const res = await fetch("/api/calcular", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(body),
  });

  if (!res.ok) return alert("Erro ao calcular.");
  const d = await res.json();

  $("r-final").textContent = moeda(d.valor_final);
  $("r-cashback").textContent = moeda(d.cashback_final);

  const tags = [];
  if (d.bonus_vip_aplicado) tags.push("⭐ Bônus VIP +10%");
  if (d.promocao_aplicada) tags.push("🎉 Promoção 2x");
  $("r-tags").textContent = tags.join(" · ");

  $("resultado").classList.remove("hidden");
  carregarHistorico();
});

async function carregarHistorico() {
  const res = await fetch("/api/historico");
  const data = await res.json();

  if (!data.length) {
    $("vazio").classList.remove("hidden");
    return;
  }

  $("vazio").classList.add("hidden");
  $("historico").innerHTML = data
    .map((r) => `<tr>
      <td>${r.tipo_cliente}</td>
      <td>${moeda(r.valor_compra)}</td>
      <td>${(r.desconto * 100).toFixed(0)}%</td>
      <td>${moeda(r.valor_final)}</td>
      <td><strong>${moeda(r.cashback)}</strong></td>
      <td>${new Date(r.criado_em).toLocaleDateString("pt-BR")}</td>
    </tr>`)
    .join("");
}

carregarHistorico();
