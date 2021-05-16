
from Veiculo import Veiculo

class Acesso:
    def __init__(self, id_acesso : str, veiculo : Veiculo, hora_entrada : int, hora_saida : int):
        self.id_acesso = id_acesso
        self.veiculo = veiculo
        self.hora_entrada = hora_entrada
        self.hora_saida = hora_saida

    def getPrecoFinal(self):
        return

    def printClass(self):
        print("ID Acesso " + self.id_acesso)    
        print("Hora Entrada " + self.hora_entrada)    
        print("Hora Saida" + self.hora_saida)  
        self.veiculo.printClass()    
    