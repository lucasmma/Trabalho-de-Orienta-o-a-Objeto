import Endereco

class PessoaFisica:
    def __init__(self , cnh : int, nome_completo : str, telefone_celular : str, telefone_residencial : str, endereco : Endereco):
        self.cnh = cnh
        self.nome_completo = nome_completo
        self.telefone_celular = telefone_celular
        self.telefone_residencial = telefone_residencial
        self.endereco = endereco

    def printClass(self):
        print("CNH " + self.cnh)
        print("Nome Completo " + self.nome_completo)
        print("Telefone Celular " + self.telefone_celular)
        print("Telefone Residencial " + self.telefone_residencial)
        self.endereco.printClass()