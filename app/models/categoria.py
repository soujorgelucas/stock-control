class Categoria:
    def __init__(self, id_categoria=None, nome=None, descricao=None):
        self.id_categoria = id_categoria
        self.nome = nome
        self.descricao = descricao

    def to_dict(self):
        return {
            "id_categoria": self.id_categoria,
            "nome": self.nome,
            "descricao": self.descricao
        }
