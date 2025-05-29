# 🧾 Sistema de Caixa - Padaria

Este projeto é um sistema simples de caixa para uma padaria, com interface web e backend em Flask.  
Ele permite listar produtos disponíveis, adicionar produtos a um pedido, finalizar o pedido e visualizar o total de vendas acumulado.

---

## 📚 Índice

- [Descrição](#-descrição)
- [Funcionalidades](#-funcionalidades)
- [Tecnologias Utilizadas](#️-tecnologias-utilizadas)
- [Estrutura do Projeto](#-estrutura-do-projeto)
- [Como Executar](#-como-executar)
- [Contribuindo](#-contribuindo)
- [Licença](#-licença)

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

**Frontend:**  
- HTML5  
- CSS (via Bootstrap 5)  
- JavaScript (Fetch API)  

**Backend:**  
- Python 3  
- Flask  
- Organização em `routes/`, `models/`, `templates/`, `static/`  

---

## 📁 Estrutura do Projeto

```
padaria_sistema/
├── frontend/          # Arquivos HTML/JS separados (opcional)
├── models/            # Lógica de dados e manipulação
├── routes/            # Rotas da API Flask
├── static/            # Arquivos estáticos (JS, CSS, imagens)
├── templates/         # Templates HTML para Flask
├── app.py             # Arquivo principal que roda o servidor
├── requirements.txt   # Dependências Python
└── README.md          # Este arquivo
```

---

## 🚀 Como Executar

1. Clone este repositório:
   ```bash
   git clone https://github.com/fmoreira10/ProjetoGit.git
   ```
2. Navegue até o diretório do projeto:
   ```bash
   cd ProjetoGit
   ```
3. (Opcional) Crie e ative um ambiente virtual:
   - Linux/macOS:
     ```bash
     python3 -m venv venv
     source venv/bin/activate
     ```
   - Windows:
     ```bash
     python -m venv venv
     venv\Scripts\activate
     ```
4. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```
5. Execute o sistema:
   ```bash
   python app.py
   ```
6. Abra o navegador e acesse:
   ```
   http://localhost:5000
   ```

---

## 🤝 Contribuindo

Contribuições são muito bem-vindas!  

Para contribuir:  

1. Faça um fork deste repositório.  
2. Crie uma branch para sua feature:
   ```bash
   git checkout -b feature/nome-da-feature
   ```
3. Faça commit das suas alterações:
   ```bash
   git commit -m "Descrição da feature"
   ```
4. Envie para o repositório remoto:
   ```bash
   git push origin feature/nome-da-feature
   ```
5. Abra um Pull Request aqui no GitHub.

---

## 📄 Licença

Este projeto está licenciado sob a Licença MIT — veja o arquivo [LICENSE](LICENSE) para mais detalhes.
