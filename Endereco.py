

class Endereco:
    def __init__(self, uf : str, cidade : str, bairro : str, endereco : str, complemento : str):
        self.uf = uf
        self.cidade = cidade
        self.bairro = bairro
        self.endereco = endereco
        self.complemento = complemento

    def printClass(self):
        print("UF " + self.uf)
        print("Cidade " + self.cidade)
        print("Bairro " + self.bairro)
        print("Endereco " + self.endereco)
        print("Complemento " + self.complemento)