class Fornecedor:
    def __init__(self, id_fornecedor=None, nome=None, cnpj=None, telefone=None, email=None):
        self.id_fornecedor = id_fornecedor
        self.nome = nome
        self.cnpj = cnpj
        self.telefone = telefone
        self.email = email

    def to_dict(self):
        return {
            "id_fornecedor": self.id_fornecedor,
            "nome": self.nome,
            "cnpj": self.cnpj,
            "telefone": self.telefone,
            "email": self.email
        }
