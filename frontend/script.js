const API = "http://127.0.0.1:5000";

async function listarProdutos() {
  const res = await fetch(`${API}/produtos`);
  const produtos = await res.json();

  const lista = document.getElementById("lista-produtos");
  lista.innerHTML = "";

  produtos.forEach(p => {
    const li = document.createElement("li");
    li.className = "list-group-item";
    li.textContent = `${p.nome} - R$ ${p.preco.toFixed(2)} (${p.quantidade} unid.)`;
    lista.appendChild(li);
  });
}

async function adicionarAoPedido() {
  const nome = document.getElementById("nome-produto").value;
  const quantidade = parseInt(document.getElementById("quantidade").value);

  const res = await fetch(`${API}/pedido`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ nome, quantidade })
  });

  const data = await res.json();
  alert(data.mensagem || data.erro);
}

async function finalizarPedido() {
  const res = await fetch(`${API}/pedido/finalizar`, {
    method: "POST"
  });

  const data = await res.json();
  alert(`Pedido finalizado!\nValor total: R$ ${data.valor_total.toFixed(2)}`);
  atualizarTotalVendas();
}

async function atualizarTotalVendas() {
  const res = await fetch(`${API}/vendas`);
  const data = await res.json();
  document.getElementById("total-vendas").textContent = `R$ ${data.total_vendas.toFixed(2)}`;
}

listarProdutos();
atualizarTotalVendas();
