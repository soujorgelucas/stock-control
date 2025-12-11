from app.config.database import get_connection
from app.models.fornecedor import Fornecedor

# LISTAR FORNECEDORES
def listar_fornecedores():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    
    cursor.execute("SELECT * FROM fornecedor")
    rows = cursor.fetchall()
    
    fornecedores = [Fornecedor(
        id_fornecedor=row['id_fornecedor'],
        nome=row['nome'],
        cnpj=row['cnpj'],
        telefone=row['telefone'],
        email=row['email']
    ) for row in rows]
    
    cursor.close()
    conn.close()
    return fornecedores

# CRIAR FORNECEDOR
def criar_fornecedor(fornecedor: Fornecedor):
    conn = get_connection()
    cursor = conn.cursor()
    
    sql = "INSERT INTO fornecedor (nome, cnpj, telefone, email) VALUES (%s, %s, %s, %s)"
    cursor.execute(sql, (fornecedor.nome, fornecedor.cnpj, fornecedor.telefone, fornecedor.email))
    conn.commit()
    fornecedor_id = cursor.lastrowid
    
    cursor.close()
    conn.close()
    return fornecedor_id

# BUSCAR POR ID
def buscar_fornecedor_por_id(fornecedor_id):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    
    cursor.execute("SELECT * FROM fornecedor WHERE id_fornecedor = %s", (fornecedor_id,))
    row = cursor.fetchone()
    
    cursor.close()
    conn.close()
    
    if row:
        return Fornecedor(
            id_fornecedor=row['id_fornecedor'],
            nome=row['nome'],
            cnpj=row['cnpj'],
            telefone=row['telefone'],
            email=row['email']
        )
    return None

# ATUALIZAR FORNECEDOR
def atualizar_fornecedor(fornecedor: Fornecedor):
    conn = get_connection()
    cursor = conn.cursor()
    
    sql = "UPDATE fornecedor SET nome=%s, cnpj=%s, telefone=%s, email=%s WHERE id_fornecedor=%s"
    cursor.execute(sql, (fornecedor.nome, fornecedor.cnpj, fornecedor.telefone, fornecedor.email, fornecedor.id_fornecedor))
    conn.commit()
    
    cursor.close()
    conn.close()
    return True

# DELETAR FORNECEDOR
def deletar_fornecedor(fornecedor_id):
    conn = get_connection()
    cursor = conn.cursor()
    
    cursor.execute("DELETE FROM fornecedor WHERE id_fornecedor = %s", (fornecedor_id,))
    conn.commit()
    
    cursor.close()
    conn.close()
    return True
