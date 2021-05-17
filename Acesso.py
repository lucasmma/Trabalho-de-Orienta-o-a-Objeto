
from Veiculo import Veiculo
from Utils import horario_abre, horario_fecha, dia_inteiro
from math import floor

class Acesso:
    def __init__(self, id_acesso : str, veiculo : Veiculo, hora_entrada : int, hora_saida : int):
        self.id_acesso = id_acesso
        self.veiculo = veiculo
        self.hora_entrada = hora_entrada
        self.hora_saida = hora_saida

    def getPrecoFinal(self):
        #Terminar a função de preço final
        #6:00 - 20:00
        # minuto normal = 0.5
        # 15 min = desconto 0.5
        # 1 hora = desconto 1
        # 9 horas = diaria = 110 reais (resto do tempo da diaria = 0.2 por minuto)
        # pernoite = 30
        preco_final = 0
        dia_entrada = floor(self.hora_entrada / dia_inteiro)
        dia_saida = floor(self.hora_saida / dia_inteiro)
        if dia_entrada == dia_saida:
            #Não possui pernoite
            preco_final = self.getPrecoDoMesmoDia(self.hora_entrada, self.hora_saida)
        else:
            ##calculo com pernoite
            hora_final_dia_inicial = (dia_entrada * dia_inteiro) + horario_fecha
            hora_inicial_dia_final = (dia_saida * dia_inteiro) + horario_abre
            preco_final += (dia_saida - dia_entrada) * 30
            print((dia_saida - dia_entrada) * 30)
            preco_final += ((dia_saida - dia_entrada) - 1) * (110 + (5 * 60 * 0.2) - 15)
            print(((dia_saida - dia_entrada) - 1) * (110 + (5 * 60 * 0.2) - 15))
            preco_final += self.getPrecoDoMesmoDia(self.hora_entrada, hora_final_dia_inicial)
            print(self.getPrecoDoMesmoDia(self.hora_entrada, hora_final_dia_inicial))
            preco_final += self.getPrecoDoMesmoDia(hora_inicial_dia_final, self.hora_saida)
            print(self.getPrecoDoMesmoDia(hora_inicial_dia_final, self.hora_saida))

            pass
        return preco_final

    def getPrecoDoMesmoDia(self,hora_entrada_dia, hora_saida_dia):
        dia_entrada = floor(hora_entrada_dia / dia_inteiro)
        dia_saida = floor(hora_saida_dia / dia_inteiro)
        if dia_entrada != dia_saida:
            print("Dias diferentes entre entrada e saida")
            return 0
        
        diferenca_de_horario = int(hora_saida_dia - hora_entrada_dia)
        preco_final = 0
        if diferenca_de_horario < 32400:
            preco_final += floor(diferenca_de_horario/60) * 0.5
            preco_final -= floor(diferenca_de_horario/900)
            preco_final -= floor(diferenca_de_horario/3600)
        else:
            diferenca_de_horario -= 32400
            preco_final += 110
            preco_final += floor(diferenca_de_horario/60) * 0.2
        return preco_final


    def printClass(self):
        print("\tID Acesso " + self.id_acesso)    
        print("\tHora Entrada " + str(self.hora_entrada))
        print("\tHora Saida " + str(self.hora_saida))
        if self.hora_saida != None:
            print("\tPreço Final " + str(self.getPrecoFinal()))
        self.veiculo.printClass()
    
    def setHorarioSaida(self, hora_saida):
        self.hora_saida = hora_saida
    
    def validarHorarios(self):
        return self.hora_saida > self.hora_entrada