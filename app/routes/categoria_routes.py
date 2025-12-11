from flask import Blueprint, request, jsonify
from app.repositories.categoria_repo import listar_categorias, criar_categoria, buscar_categoria_por_id, atualizar_categoria, deletar_categoria
from app.models.categoria import Categoria

categoria_bp = Blueprint("categoria_bp", __name__)

@categoria_bp.get("/")
def get_categorias():
    categorias = listar_categorias()
    return jsonify([c.to_dict() for c in categorias])

@categoria_bp.get("/<int:id_categoria>")
def get_categoria(id_categoria):
    c = buscar_categoria_por_id(id_categoria)
    if c:
        return jsonify(c.to_dict())
    return jsonify({"error": "Categoria não encontrada"}), 404

@categoria_bp.post("/")
def post_categoria():
    data = request.json
    c = Categoria(nome=data.get("nome"), descricao=data.get("descricao"))
    categoria_id = criar_categoria(c)
    return jsonify({"id_categoria": categoria_id}), 201

@categoria_bp.put("/<int:id_categoria>")
def put_categoria(id_categoria):
    c = buscar_categoria_por_id(id_categoria)
    if not c:
        return jsonify({"error": "Categoria não encontrada"}), 404
    data = request.json
    c.nome = data.get("nome", c.nome)
    c.descricao = data.get("descricao", c.descricao)
    atualizar_categoria(c)
    return jsonify({"message": "Categoria atualizada com sucesso"})

@categoria_bp.delete("/<int:id_categoria>")
def delete_categoria(id_categoria):
    c = buscar_categoria_por_id(id_categoria)
    if not c:
        return jsonify({"error": "Categoria não encontrada"}), 404
    deletar_categoria(id_categoria)
    return jsonify({"message": "Categoria deletada com sucesso"})
