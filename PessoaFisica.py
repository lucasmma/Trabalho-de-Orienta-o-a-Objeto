import Endereco

class PessoaFisica:
    def __init__(self , id_pessoa_fisica : int, nome_completo : str, telefone_celular : str, telefone_residencial : str, endereco : Endereco, is_mensalista : bool):
        self.id_pessoa_fisica = id_pessoa_fisica
        self.nome_completo = nome_completo
        self.telefone_celular = telefone_celular
        self.telefone_residencial = telefone_residencial
        self.endereco = endereco
        self.is_mensalista = is_mensalista

    def printClass(self):
        print(self.id_pessoa_fisica)
        print(self.nome_completo)
        print(self.telefone_celular)
        print(self.telefone_residencial)
        self.endereco.printClass()
        print(self.is_mensalista)