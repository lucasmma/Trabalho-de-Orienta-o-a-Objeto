

class Endereco:
    def __init__(self, id_endereco, uf, cidade, bairro, endereco, complemento):
        self.id_endereco = id_endereco
        self.uf = uf
        self.cidade = cidade
        self.bairro = bairro
        self.endereco = endereco
        self.complemento = complemento

    def printClass(self):
        print(self.id_endereco)
        print(self.uf)
        print(self.cidade)
        print(self.bairro)
        print(self.endereco)
        print(self.complemento)