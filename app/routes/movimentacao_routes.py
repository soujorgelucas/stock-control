from flask import Blueprint, request, jsonify
from app.services.estoque_service import movimentar_estoque
from app.repositories.movimentacao_repo import listar_movimentacoes, buscar_movimentacao_por_id

movimentacao_bp = Blueprint("movimentacao_bp", __name__)

@movimentacao_bp.get("/")
def get_movimentacoes():
    movs = listar_movimentacoes()
    return jsonify([m.to_dict() for m in movs])

@movimentacao_bp.get("/<int:id_movimentacao>")
def get_movimentacao(id_movimentacao):
    m = buscar_movimentacao_por_id(id_movimentacao)
    if m:
        return jsonify(m.to_dict())
    return jsonify({"error": "Movimentação não encontrada"}), 404

@movimentacao_bp.post("/")
def post_movimentacao():
    data = request.json
    mov_id, msg = movimentar_estoque(
        id_produto=data.get("id_produto"),
        tipo=data.get("tipo_movimentacao"),
        quantidade=data.get("quantidade"),
        observacao=data.get("observacao", "")
    )
    if not mov_id:
        return jsonify({"error": msg}), 400
    return jsonify({"id_movimentacao": mov_id, "message": msg}), 201
