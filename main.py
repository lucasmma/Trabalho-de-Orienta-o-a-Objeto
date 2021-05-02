# main.py
from Endereco import Endereco
from PessoaFisica import PessoaFisica
from Veiculo import Veiculo
from Acesso import Acesso

def main():
    endereco = Endereco(0, 1, 2 , 3, 4, 5)
    endereco.printClass()

if __name__ == "__main__":
    main()