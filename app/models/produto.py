class Produto:
    def __init__(self, id_produto=None, nome=None, descricao=None, id_categoria=None,
                 id_fornecedor=None, quantidade_atual=0, preco_custo=0.0, preco_venda=0.0):
        self.id_produto = id_produto
        self.nome = nome
        self.descricao = descricao
        self.id_categoria = id_categoria
        self.id_fornecedor = id_fornecedor
        self.quantidade_atual = quantidade_atual
        self.preco_custo = preco_custo
        self.preco_venda = preco_venda

    def to_dict(self):
        return {
            "id_produto": self.id_produto,
            "nome": self.nome,
            "descricao": self.descricao,
            "id_categoria": self.id_categoria,
            "id_fornecedor": self.id_fornecedor,
            "quantidade_atual": self.quantidade_atual,
            "preco_custo": self.preco_custo,
            "preco_venda": self.preco_venda
        }
