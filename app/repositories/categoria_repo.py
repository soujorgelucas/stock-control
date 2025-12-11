from app.config.database import get_connection
from app.models.categoria import Categoria

# LISTAR TODAS AS CATEGORIAS
def listar_categorias():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    
    cursor.execute("SELECT * FROM categoria")
    rows = cursor.fetchall()
    
    categorias = [Categoria(id_categoria=row['id_categoria'], nome=row['nome'], descricao=row['descricao']) for row in rows]
    
    cursor.close()
    conn.close()
    return categorias

# CRIAR CATEGORIA
def criar_categoria(categoria: Categoria):
    conn = get_connection()
    cursor = conn.cursor()
    
    sql = "INSERT INTO categoria (nome, descricao) VALUES (%s, %s)"
    cursor.execute(sql, (categoria.nome, categoria.descricao))
    conn.commit()
    categoria_id = cursor.lastrowid
    
    cursor.close()
    conn.close()
    return categoria_id

# BUSCAR POR ID
def buscar_categoria_por_id(categoria_id):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    
    cursor.execute("SELECT * FROM categoria WHERE id_categoria = %s", (categoria_id,))
    row = cursor.fetchone()
    
    cursor.close()
    conn.close()
    
    if row:
        return Categoria(id_categoria=row['id_categoria'], nome=row['nome'], descricao=row['descricao'])
    return None

# ATUALIZAR CATEGORIA
def atualizar_categoria(categoria: Categoria):
    conn = get_connection()
    cursor = conn.cursor()
    
    sql = "UPDATE categoria SET nome=%s, descricao=%s WHERE id_categoria=%s"
    cursor.execute(sql, (categoria.nome, categoria.descricao, categoria.id_categoria))
    conn.commit()
    
    cursor.close()
    conn.close()
    return True

# DELETAR CATEGORIA
def deletar_categoria(categoria_id):
    conn = get_connection()
    cursor = conn.cursor()
    
    cursor.execute("DELETE FROM categoria WHERE id_categoria = %s", (categoria_id,))
    conn.commit()
    
    cursor.close()
    conn.close()
    return True
