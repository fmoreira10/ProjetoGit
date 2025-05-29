# models/classes.py

class Produto:
    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

    def to_dict(self):
        return {
            "nome": self.nome,
            "preco": self.preco,
            "quantidade": self.quantidade
        }

# Adicione essas abaixo:

class Pedido:
    def __init__(self):
        self.itens = []

    def adicionar_item(self, produto):
        self.itens.append(produto)

    def to_dict(self):
        return {
            "itens": [produto.to_dict() for produto in self.itens]
        }

class Caixa:
    def __init__(self):
        self.pedidos = []

    def finalizar_pedido(self, pedido):
        self.pedidos.append(pedido)

    def total_vendas(self):
        return sum(p.preco * p.quantidade for pedido in self.pedidos for p in pedido.itens)

