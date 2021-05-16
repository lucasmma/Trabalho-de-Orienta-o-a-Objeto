class Veiculo:
    def __init__(self, cnh : int, marca : str, modelo : str, numero_da_placa : str):
        self.cnh = cnh
        self.marca = marca
        self.modelo = modelo
        self.numero_da_placa = numero_da_placa

    def printClass(self):
        print("CNH " + self.cnh)
        print("Marca " + self.marca)
        print("Modelo " + self.modelo)
        print("Placa " + self.numero_da_placa)