# routes/caixa_routes.py
from flask import Blueprint, jsonify, request
from models.classes import Produto, Pedido, Caixa

caixa_bp = Blueprint("caixa", __name__)

# Dados em memória (por enquanto)
estoque = []
pedido_atual = Pedido()
caixa = Caixa()

@caixa_bp.route("/produtos", methods=["GET"])
def listar_produtos():
    return jsonify([p.to_dict() for p in estoque])

@caixa_bp.route("/produtos", methods=["POST"])
def adicionar_produto():
    data = request.get_json()
    produto = Produto(data["nome"], float(data["preco"]), int(data["quantidade"]))
    estoque.append(produto)
    return jsonify({"mensagem": "Produto adicionado com sucesso!"})

@caixa_bp.route("/pedido", methods=["POST"])
def adicionar_ao_pedido():
    data = request.get_json()
    for p in estoque:
        if p.nome == data["nome"]:
            pedido_atual.adicionar_produto(p, int(data["quantidade"]))
            return jsonify({"mensagem": f"{data['quantidade']}x {p.nome} adicionados ao pedido!"})
    return jsonify({"erro": "Produto não encontrado"}), 404

@caixa_bp.route("/pedido/finalizar", methods=["POST"])
def finalizar_pedido():
    valor = pedido_atual.total()
    caixa.registrar_pedido(pedido_atual)
    pedido_atual.produtos = []
    return jsonify({"mensagem": "Pedido finalizado!", "valor_total": valor})
