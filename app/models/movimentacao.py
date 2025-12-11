class Movimentacao:
    def __init__(self, id_movimentacao=None, id_produto=None, tipo_movimentacao=None,
                 quantidade=0, data_movimentacao=None, observacao=None):
        self.id_movimentacao = id_movimentacao
        self.id_produto = id_produto
        self.tipo_movimentacao = tipo_movimentacao  # 'entrada' ou 'saida'
        self.quantidade = quantidade
        self.data_movimentacao = data_movimentacao
        self.observacao = observacao

    def to_dict(self):
        return {
            "id_movimentacao": self.id_movimentacao,
            "id_produto": self.id_produto,
            "tipo_movimentacao": self.tipo_movimentacao,
            "quantidade": self.quantidade,
            "data_movimentacao": self.data_movimentacao,
            "observacao": self.observacao
        }
