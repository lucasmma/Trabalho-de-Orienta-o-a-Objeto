class Error(Exception):
    """Base class for other exceptions"""
    pass

class InvalidMenuNumber(Error):
    "Selecionado quando o valor é invalido no menu"
    pass

class PlacaInvalida(Error):
    "Mask de placa invalida"
    pass

class DadosVeiculosIncompletosException(Error):
    "Dados do veiculo incompleto"