class Error(Exception):
    """Base class for other exceptions"""
    pass

class InvalidMenuNumberException(Error):
    "Selecionado quando o valor é invalido no menu"
    pass

class PlacaInvalidaException(Error):
    "Mask de placa invalida"
    pass

class DadosVeiculosIncompletosException(Error):
    "Dados do veiculo incompleto"
    pass

class DadosAcessoIncompletosException(Error):
    "Dados de Acesso incompleto"
    pass

class DadosPessoaisIncompletosException(Error):
    "Dados pessoais das pessoas fisicas incompleto"
    pass

class EstacionamentoFechadoException(Error):
    "Estacionamento Fechado"
    pass


class VeiculoDuplicadoException(Error):
    "Veiculo Duplicado"
    pass

class PessoaFisicaDuplicadaException(Error):
    "Veiculo Duplicado"
    pass

class DadosAcessoIncompletosException(Error):
    "Dados acessos incompletos/errados"
    pass

class VeiculoNaoEncontradoException(Error):
    "Veiculo não encontrado no estacionamento"
    pass

class PeriodoInvalidoException(Error):
    "Periodo de tempo invalido, horario saida maior ou igual horario entrada"
    pass