from flask import Blueprint, request, jsonify
from app.repositories.produto_repo import listar_produtos, criar_produto, buscar_produto_por_id, atualizar_produto, deletar_produto
from app.models.produto import Produto

produto_bp = Blueprint("produto_bp", __name__)

# LISTAR PRODUTOS
@produto_bp.get("/")
def get_produtos():
    produtos = listar_produtos()
    return jsonify([p.to_dict() for p in produtos])

# BUSCAR PRODUTO POR ID
@produto_bp.get("/<int:id_produto>")
def get_produto(id_produto):
    p = buscar_produto_por_id(id_produto)
    if p:
        return jsonify(p.to_dict())
    return jsonify({"error": "Produto não encontrado"}), 404

# CRIAR PRODUTO
@produto_bp.post("/")
def post_produto():
    data = request.json
    p = Produto(
        nome=data.get("nome"),
        descricao=data.get("descricao"),
        id_categoria=data.get("id_categoria"),
        id_fornecedor=data.get("id_fornecedor"),
        quantidade_atual=data.get("quantidade_atual", 0),
        preco_custo=data.get("preco_custo", 0.0),
        preco_venda=data.get("preco_venda", 0.0)
    )
    produto_id = criar_produto(p)
    return jsonify({"id_produto": produto_id}), 201

# ATUALIZAR PRODUTO
@produto_bp.put("/<int:id_produto>")
def put_produto(id_produto):
    data = request.json
    p = buscar_produto_por_id(id_produto)
    if not p:
        return jsonify({"error": "Produto não encontrado"}), 404

    p.nome = data.get("nome", p.nome)
    p.descricao = data.get("descricao", p.descricao)
    p.id_categoria = data.get("id_categoria", p.id_categoria)
    p.id_fornecedor = data.get("id_fornecedor", p.id_fornecedor)
    p.quantidade_atual = data.get("quantidade_atual", p.quantidade_atual)
    p.preco_custo = data.get("preco_custo", p.preco_custo)
    p.preco_venda = data.get("preco_venda", p.preco_venda)

    atualizar_produto(p)
    return jsonify({"message": "Produto atualizado com sucesso"})

# DELETAR PRODUTO
@produto_bp.delete("/<int:id_produto>")
def delete_produto(id_produto):
    p = buscar_produto_por_id(id_produto)
    if not p:
        return jsonify({"error": "Produto não encontrado"}), 404
    deletar_produto(id_produto)
    return jsonify({"message": "Produto deletado com sucesso"})
