import Endereco

class PessoaFisica:
    def __init__(self, id_pessoa_fisica, nome_completo, telefone_celular, telefone_residencial, endereco, is_mensalista):
        self.id_pessoa_fisica = id_pessoa_fisica
        self.nome_completo = nome_completo
        self.telefone_celular = telefone_celular
        self.telefone_residencial = telefone_residencial
        self.endereco = endereco
        self.is_mensalista = is_mensalista
