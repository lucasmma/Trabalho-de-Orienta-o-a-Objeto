class Veiculo:
    def __init__(self, cnh : int, marca : str, modelo : str, numero_da_placa : str):
        self.cnh = cnh
        self.marca = marca
        self.modelo = modelo
        self.numero_da_placa = numero_da_placa

    def printClass(self):
        print("\tCNH " + str(self.cnh))
        print("\tMarca " + self.marca)
        print("\tModelo " + self.modelo)
        print("\tPlaca " + self.numero_da_placa)