# 🧾 Sistema de Caixa - Padaria

Este projeto é um sistema simples de caixa para uma padaria, com interface web e backend em Flask. Ele permite listar produtos disponíveis, adicionar produtos a um pedido, finalizar o pedido e visualizar o total de vendas acumulado.

---

## 📌 Funcionalidades

- 🔄 Listar produtos disponíveis
- ➕ Adicionar produtos e quantidade ao pedido
- ✅ Finalizar pedido com cálculo do valor total
- 💰 Exibir total de vendas acumulado
- 🧠 Backend estruturado com Flask e rotas RESTful
- 🎨 Interface simples e responsiva com Bootstrap 5

---

## 🛠️ Tecnologias Utilizadas

### Frontend:
- HTML5
- CSS (via [Bootstrap 5](https://getbootstrap.com/))
- JavaScript (fetch API)

---

### Backend:
- Python 3
- Flask
- Organização em `routes/`, `models/`, `templates/`, `static/`

---

## 📁 Estrutura do Projeto

```bash
padaria_sistema/
├── frontend/          # Arquivos HTML/JS separados (opcional)
├── models/            # Lógica de dados e manipulação
├── routes/            # Rotas da API Flask
├── static/            # Arquivos estáticos (JS, CSS, imagens)
├── templates/         # Templates HTML para Flask
├── app.py             # Arquivo principal que roda o servidor
├── requirements.txt   # Dependências Python
└── README.md
