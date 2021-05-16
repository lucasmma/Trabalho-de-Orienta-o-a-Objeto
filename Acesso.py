
class Acesso:
    def __init__(self, id_acesso : int, id_veiculo : int, hora_entrada : int, hora_saida : int):
        self.id_acesso = id_acesso
        self.id_veiculo = id_veiculo
        self.hora_entrada = hora_entrada
        self.hora_saida = hora_saida

    def getPrecoFinal(self):
        return

    def printClass(self):
        print(self.id_acesso)    
        print(self.id_veiculo)    
        print(self.hora_entrada)    
        print(self.hora_saida)    
    