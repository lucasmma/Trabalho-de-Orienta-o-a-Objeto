

class Endereco:
    def __init__(self, uf : str, cidade : str, bairro : str, endereco : str, complemento : str):
        self.uf = uf
        self.cidade = cidade
        self.bairro = bairro
        self.endereco = endereco
        self.complemento = complemento

    def printClass(self):
        print("\tUF " + self.uf)
        print("\tCidade " + self.cidade)
        print("\tBairro " + self.bairro)
        print("\tEndereco " + self.endereco)
        print("\tComplemento " + self.complemento)