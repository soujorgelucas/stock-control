from app.config.database import get_connection
from app.models.produto import Produto

# =======================
# LISTAR TODOS OS PRODUTOS
# =======================
def listar_produtos():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    
    cursor.execute("SELECT * FROM produto")
    rows = cursor.fetchall()
    
    produtos = []
    for row in rows:
        p = Produto(
            id_produto=row['id_produto'],
            nome=row['nome'],
            descricao=row['descricao'],
            id_categoria=row['id_categoria'],
            id_fornecedor=row['id_fornecedor'],
            quantidade_atual=row['quantidade_atual'],
            preco_custo=row['preco_custo'],
            preco_venda=row['preco_venda']
        )
        produtos.append(p)
    
    cursor.close()
    conn.close()
    return produtos

# =======================
# CRIAR PRODUTO
# =======================
def criar_produto(produto: Produto):
    conn = get_connection()
    cursor = conn.cursor()
    
    sql = """
        INSERT INTO produto 
        (nome, descricao, id_categoria, id_fornecedor, quantidade_atual, preco_custo, preco_venda) 
        VALUES (%s, %s, %s, %s, %s, %s, %s)
    """
    cursor.execute(sql, (
        produto.nome,
        produto.descricao,
        produto.id_categoria,
        produto.id_fornecedor,
        produto.quantidade_atual,
        produto.preco_custo,
        produto.preco_venda
    ))
    
    conn.commit()
    produto_id = cursor.lastrowid
    
    cursor.close()
    conn.close()
    return produto_id

# =======================
# BUSCAR PRODUTO POR ID
# =======================
def buscar_produto_por_id(produto_id):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    
    cursor.execute("SELECT * FROM produto WHERE i*
