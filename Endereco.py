

class Endereco:
    def __init__(self, id_endereco : int, uf : str, cidade : str, bairro : str, endereco : str, complemento : str):
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