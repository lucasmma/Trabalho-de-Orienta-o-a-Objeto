# main.py
from Service import Service
from Endereco import Endereco
from PessoaFisica import PessoaFisica
from Veiculo import Veiculo
from Acesso import Acesso
import os
from Exceptions import InvalidMenuNumber
from Exceptions import PlacaInvalida
from Exceptions import DadosVeiculosIncompletosException
from datetime import datetime

exit = False
service = Service()

def main():
    while not exit:
        showMenu()

    print("Volte sempre ;D\n")

def clearTerminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def showMenu():
    # clearTerminal()
    print("Olá Bem vindo (de volta) ao sistema do Estacione Fácil\n\n")
    print("1 - Cadastro de Mensalista")
    print("2 - Cadastro de Entrada")
    print("3 - Cadastro de Saida")
    print("4 - Sair do Sistema\n\n")

    validarEntradaNoMenu()

def validarEntradaNoMenu():
    itemChoosen = int(input("Escolha uma opção acima: "))
    print("\n")

    try:
        if itemChoosen == 1:
            cadastrarMensalista()
        elif itemChoosen == 2:
            cadastrarEntrada()
        elif  itemChoosen == 3:
            pass
        elif itemChoosen == 4:
            global exit
            exit = True
        else:
            raise InvalidMenuNumber
    except InvalidMenuNumber:
        print("Selecione um valor válido no menu")
        validarEntradaNoMenu()

# cadastros

def cadastrarMensalista():
    
    pass

def cadastrarEntrada():
    global service

    print("Cadastro da placa do carro deve ser no seguinte formato ###-####")
    placaDoCarro = getPlacaDoCarro()
    
    veiculo = service.getVeiculo(placaDoCarro)

    if veiculo == None:
        veiculo = cadastrarVeiculo(placaDoCarro)
    
    hora_entrada = getTimeStampValue()
    
    acesso = Acesso(veiculo.numero_da_placa + hora_entrada, veiculo, hora_entrada, None)
    service.cadastrarAcesso(acesso)

def cadastrarVeiculo(placaDoCarro):
    global service
    try:
        marca = str(input("Digite a marca do carro: "))
        modelo = str(input("Digite o modelo do carro: "))
        if len(marca) == 0 or len(modelo) == 0:
            raise DadosVeiculosIncompletosException
        else:
            veiculo = Veiculo(None, marca, modelo, placaDoCarro)
            service.cadastrarVeiculo(veiculo)
            return veiculo
    except DadosVeiculosIncompletosException:
        print("Preencha todos os dados corretamente")
        return cadastrarVeiculo(placaDoCarro)

def getTimeStampValue():
    data = ""
    try:
        print("O horario deve seguir o formado (Dia)/(Mes)/(Ano) (Hora):(Minuto)")
        data = str(input("Digite a hora atual: "))
        timeformat = r"%d/%m/%y %H:%M"

        return datetime.strptime(data, timeformat).timestamp()
    except ValueError:
        print("Digite o horario corretamente, com o seguinte formato (Dia)/(Mes)/(Ano) (Hora):(Minuto)")
        return getTimeStampValue()



def getPlacaDoCarro():
    placadocarro = ""
    try:
        placadocarro = input("Digite a placa do carro: ")
        if len(placadocarro) != 8 or placadocarro[3] != "-":
            raise PlacaInvalida
        else:
            return placadocarro
    except PlacaInvalida:
        print("Digite a placa corretamente, com a seguinte mask ###-####")
        return getPlacaDoCarro()

if __name__ == "__main__":
    main()