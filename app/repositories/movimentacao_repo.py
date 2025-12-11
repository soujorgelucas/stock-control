from app.config.database import get_connection
from app.models.movimentacao import Movimentacao
from app.repositories.produto_repo import buscar_produto_por_id, atualizar_produto

# LISTAR MOVIMENTAÇÕES
def listar_movimentacoes():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    
    cursor.execute("SELECT * FROM movimentacao")
    rows = cursor.fetchall()
    
    movimentacoes = [Movimentacao(
        id_movimentacao=row['id_movimentacao'],
        id_produto=row['id_produto'],
        tipo_movimentacao=row['tipo_movimentacao'],
        quantidade=row['quantidade'],
        data_movimentacao=row['data_movimentacao'],
        observacao=row['observacao']
    ) for row in rows]
    
    cursor.close()
    conn.close()
    return movimentacoes

# CRIAR MOVIMENTAÇÃO (ATUALIZA ESTOQUE AUTOMATICAMENTE)
def criar_movimentacao(mov: Movimentacao):
    # Atualiza estoque
    produto = buscar_produto_por_id(mov.id_produto)
    if not produto:
        return None  # Produto não existe
    
    if mov.tipo_movimentacao == 'entrada':
        produto.quantidade_atual += mov.quantidade
    elif mov.tipo_movimentacao == 'saida':
        if mov.quantidade > produto.quantidade_atual:
            return None  # Estoque insuficiente
        produto.quantidade_atual -= mov.quantidade
    
    atualizar_produto(produto)
    
    # Insere movimentação
    conn = get_connection()
    cursor = conn.cursor()
    
    sql = """
        INSERT INTO movimentacao (id_produto, tipo_movimentacao, quantidade, observacao)
        VALUES (%s, %s, %s, %s)
    """
    cursor.execute(sql, (mov.id_produto, mov.tipo_movimentacao, mov.quantidade, mov.observacao))
    conn.commit()
    mov_id = cursor.lastrowid
    
    cursor.close()
    conn.close()
    return mov_id

# BUSCAR POR ID
def buscar_movimentacao_por_id(mov_id):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    
    cursor.execute("SELECT * FROM movimentacao WHERE id_movimentacao = %s", (mov_id,))
    row = cursor.fetchone()
    
    cursor.close()
    conn.close()
    
    if row:
        return Movimentacao(
            id_movimentacao=row['id_movimentacao'],
            id_produto=row['id_produto'],
            tipo_movimentacao=row['tipo_movimentacao'],
            quantidade=row['quantidade'],
            data_movimentacao=row['data_movimentacao'],
            observacao=row['observacao']
        )
    return None

# ATUALIZAR MOVIMENTAÇÃO
def atualizar_movimentacao(mov: Movimentacao):
    conn = get_connection()
    cursor = conn.cursor()
    
    sql = """
        UPDATE movimentacao SET tipo_movimentacao=%s, quantidade=%s, observacao=%s
        WHERE id_movimentacao=%s
    """
    cursor.execute(sql, (mov.tipo_movimentacao, mov.quantidade, mov.observacao, mov.id_movimentacao))
    conn.commit()
    
    cursor.close()
    conn.close()
    return True

# DELETAR MOVIMENTAÇÃO
def deletar_movimentacao(mov_id):
    conn = get_connection()
    cursor = conn.cursor()
    
    cursor.execute("DELETE FROM movimentacao WHERE id_movimentacao = %s", (mov_id,))
    conn.commit()
    
    cursor.close()
    conn.close()
    return True
