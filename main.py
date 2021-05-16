# main.py
from Service import Service
from Endereco import Endereco
from PessoaFisica import PessoaFisica
from Veiculo import Veiculo
from Acesso import Acesso
import os
from Exceptions import InvalidMenuNumber

exit = False

def main():
    while not exit:
        showMenu()

    print("Volte sempre ;D\n")

def showMenu():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Olá Bem vindo ao sistema do Estacione Fácil\n\n")
    print("1 - Cadastro de Entrada")
    print("2 - Cadastro de Saida")
    print("3 - Sair do Sistema\n\n")

    validarEntradaNoMenu()

def validarEntradaNoMenu():
    itemChoosen = int(input("Escolha uma opção acima: "))

    try:
        if itemChoosen == 1:
            pass
        elif  itemChoosen == 2:
            pass
        elif itemChoosen == 3:
            global exit
            exit = True
        else:
            raise InvalidMenuNumber
    except InvalidMenuNumber:
        print("Selecione um valor válido no menu")
        validarEntradaNoMenu()

if __name__ == "__main__":
    main()