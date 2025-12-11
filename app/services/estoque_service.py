from app.repositories.produto_repo import buscar_produto_por_id, atualizar_produto
from app.repositories.movimentacao_repo import criar_movimentacao, listar_movimentacoes
from app.models.movimentacao import Movimentacao

# ==========================
# REALIZAR MOVIMENTAÇÃO DE ESTOQUE
# ==========================
def movimentar_estoque(id_produto, tipo, quantidade, observacao=""):
    """
    Realiza entrada ou saída de produto.
    - tipo: 'entrada' ou 'saida'
    - quantidade: número inteiro positivo
    Retorna ID da movimentação ou None se falhar
    """
    produto = buscar_produto_por_id(id_produto)
    if not produto:
        return None, "Produto não encontrado"

    if tipo == 'saida' and quantidade > produto.quantidade_atual:
        return None, "Estoque insuficiente"

    mov = Movimentacao(
        id_produto=id_produto,
        tipo_movimentacao=tipo,
        quantidade=quantidade,
        observacao=observacao
    )

    mov_id = criar_movimentacao(mov)
    return mov_id, "Movimentação realizada com sucesso"

# ==========================
# VERIFICAR PRODUTOS ABAIXO DO ESTOQUE MÍNIMO
# ==========================
def produtos_estoque_baixo(minimo=5):
    """
    Retorna lista de produtos com quantidade_atual menor que o mínimo
    """
    from app.repositories.produto_repo import listar_produtos
    produtos = listar_produtos()
    return [p for p in produtos if p.quantidade_atual < minimo]

# ==========================
# CALCULAR VALOR TOTAL DO ESTOQUE
# ==========================
def valor_total_estoque():
    """
    Retorna o valor total em estoque baseado no preço de custo
    """
    from app.repositories.produto_repo import listar_produtos
    produtos = listar_produtos()
    total = sum(p.quantidade_atual * p.preco_custo for p in produtos)
    return total
