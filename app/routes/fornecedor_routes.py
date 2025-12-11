from flask import Blueprint, request, jsonify
from app.repositories.fornecedor_repo import listar_fornecedores, criar_fornecedor, buscar_fornecedor_por_id, atualizar_fornecedor, deletar_fornecedor
from app.models.fornecedor import Fornecedor

fornecedor_bp = Blueprint("fornecedor_bp", __name__)

@fornecedor_bp.get("/")
def get_fornecedores():
    fornecedores = listar_fornecedores()
    return jsonify([f.to_dict() for f in fornecedores])

@fornecedor_bp.get("/<int:id_fornecedor>")
def get_fornecedor(id_fornecedor):
    f = buscar_fornecedor_por_id(id_fornecedor)
    if f:
        return jsonify(f.to_dict())
    return jsonify({"error": "Fornecedor não encontrado"}), 404

@fornecedor_bp.post("/")
def post_fornecedor():
    data = request.json
    f = Fornecedor(
        nome=data.get("nome"),
        cnpj=data.get("cnpj"),
        telefone=data.get("telefone"),
        email=data.get("email")
    )
    fornecedor_id = criar_fornecedor(f)
    return jsonify({"id_fornecedor": fornecedor_id}), 201

@fornecedor_bp.put("/<int:id_fornecedor>")
def put_fornecedor(id_fornecedor):
    f = buscar_fornecedor_por_id(id_fornecedor)
    if not f:
        return jsonify({"error": "Fornecedor não encontrado"}), 404
    data = request.json
    f.nome = data.get("nome", f.nome)
    f.cnpj = data.get("cnpj", f.cnpj)
    f.telefone = data.get("telefone", f.telefone)
    f.email = data.get("email", f.email)
    atualizar_fornecedor(f)
    return jsonify({"message": "Fornecedor atualizado com sucesso"})

@fornecedor_bp.delete("/<int:id_fornecedor>")
def delete_fornecedor(id_fornecedor):
    f = buscar_fornecedor_por_id(id_fornecedor)
    if not f:
        return jsonify({"error": "Fornecedor não encontrado"}), 404
    deletar_fornecedor(id_fornecedor)
    return jsonify({"message": "Fornecedor deletado com sucesso"})
