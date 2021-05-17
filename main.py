# main.py
from Service import Service
from Endereco import Endereco
from PessoaFisica import PessoaFisica
from Veiculo import Veiculo
from Acesso import Acesso
import os
from Exceptions import DadosAcessoIncompletosException, InvalidMenuNumberException
from Exceptions import PlacaInvalidaException
from Exceptions import DadosVeiculosIncompletosException
from Exceptions import DadosPessoaisIncompletosException
from Exceptions import EstacionamentoFechadoException
from Exceptions import VeiculoDuplicadoException
from Exceptions import PessoaFisicaDuplicadaException
from Exceptions import VeiculoNaoEncontradoException
from Exceptions import PeriodoInvalidoException
import datetime

exit = False
service = Service()
horario_abre = 21600
horario_fecha = 72000
dia_inteiro = 86400

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

    #COMANDO PRA LISTAR AS ENTIDADES

    validarEntradaNoMenu()

def validarEntradaNoMenu():
    itemChoosen = int(input("Escolha uma opção acima: "))
    print("\n")

    try:
        if itemChoosen == 1:
            cadastrarMensalista()
        elif itemChoosen == 2:
            registrarEntrada()
        elif  itemChoosen == 3:
            registrarSaida()
        elif itemChoosen == 4:
            global exit
            exit = True
        else:
            raise InvalidMenuNumberException
    except InvalidMenuNumberException:
        print("Selecione um valor válido no menu")
        validarEntradaNoMenu()

# cadastros

def cadastrarMensalista():
    global service
    try:
        cnh = str(input("Digite o numero da sua CNH: "))

        pfCadastrada = service.getPessoaFisica(int(cnh))

        if pfCadastrada != None:
            raise PessoaFisicaDuplicadaException
        
        nome_completo = str(input("Digite seu nome Completo: "))
        telefone_celular = str(input("Digite seu telefone Celular: "))
        telefone_residencial = str(input("Digite seu telefone residencial: "))
        endereco = cadastrarEndereco()

        if len(cnh) == 0 or len(nome_completo) == 0 or len(telefone_celular) == 0 or len(telefone_residencial) == 0:
            raise DadosPessoaisIncompletosException

        pessoafisica = PessoaFisica(int(cnh), nome_completo, telefone_celular, telefone_residencial, endereco)
        service.cadastrarPessoaFisica(pessoafisica)

    except DadosPessoaisIncompletosException:
        print("Cadastro os dados corretamente")
        return cadastrarMensalista()
    
    except PessoaFisicaDuplicadaException:
        print("CNH inválida (Pessoa já cadastrada)\n")
        return cadastrarMensalista()

def cadastrarEndereco():
    try:
        uf = str(input("Digite o seu UF: "))
        cidade = str(input("Digite a sua cidade: "))
        bairro = str(input("Digite o seu bairro: "))
        endereco = str(input("Digite o seu endereço: "))
        complemento = str(input("Digite o seu complemento: "))
        if len(uf) == 0 or len(cidade) == 0 or len(bairro) == 0 or len(endereco) == 0 or len(complemento) == 0:
            raise DadosPessoaisIncompletosException
        else: 
            return Endereco(uf,cidade,bairro,endereco,complemento)
    except DadosPessoaisIncompletosException:
        print("Cadastro os dados do Endereco corretamente")
        return cadastrarEndereco()

def registrarEntrada():
    global service

    
    print("Cadastro da placa do carro deve ser no seguinte formato ###-####")
    placaDoCarro = getPlacaDoCarro()

    try:
        veiculo = service.getVeiculo(placaDoCarro)

        if veiculo == None:
            veiculo = cadastrarVeiculo(placaDoCarro)
            hora_entrada = getTimeStampValue()
                
            acesso = Acesso(veiculo.numero_da_placa + str(hora_entrada), veiculo, hora_entrada, None)
            service.cadastrarAcesso(acesso)
        else:
            raise VeiculoDuplicadoException

    except VeiculoDuplicadoException:
        print("Placa do veículo inválida (Veiculo já se encontra estacionado)\n")
        registrarEntrada()

def registrarSaida():
    global service
    
    print("Cadastro da placa do carro deve ser no seguinte formato ###-####")
    placaDoCarro = getPlacaDoCarro() 

    try:
        veiculo = service.getVeiculo(placaDoCarro)

        if veiculo == None:
            raise VeiculoNaoEncontradoException
        else:
            hora_saida = getTimeStampValue()
            acesso = service.getAcesso(veiculo.numero_da_placa)
            
            if acesso == None:
                raise DadosAcessoIncompletosException

            acesso.setHorarioSaida(hora_saida)
            if not acesso.validarHorarios():
                raise PeriodoInvalidoException


            #Terminar a função de preço final
            print("\nO preço total a ser pago será: R$" + str(acesso.getPrecoFinal()) + "\n\n")
                
            


    except VeiculoNaoEncontradoException:
        print("Placa inválida (O veículo não se encontra estacionado)\n")
        registrarSaida()
    
    except DadosAcessoIncompletosException:
        print("Acesso não encontrado")
        registrarSaida()
    
    except PeriodoInvalidoException:
        print("A saida deve ocorrer depois da entrada")
        registrarSaida()

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
        timestampEntrada =  datetime.datetime.strptime(data, timeformat).replace(tzinfo=datetime.timezone.utc).astimezone(tz=None).timestamp()
        
        if (timestampEntrada % dia_inteiro) < horario_abre or (timestampEntrada % dia_inteiro) > horario_fecha:
            raise EstacionamentoFechadoException
        else:
            return timestampEntrada

    except ValueError:
        print("Digite o horario corretamente, com o seguinte formato (Dia)/(Mes)/(Ano) (Hora):(Minuto)")
        return getTimeStampValue()
    except EstacionamentoFechadoException:
        print("O estacionamento abre 6 horas e fecha 20 horas")
        return getTimeStampValue()


def getPlacaDoCarro():
    placadocarro = ""
    try:
        placadocarro = input("Digite a placa do carro: ")
        if len(placadocarro) != 8 or placadocarro[3] != "-":
            raise PlacaInvalidaException
        else:
            return placadocarro
    except PlacaInvalidaException:
        print("Digite a placa corretamente, com a seguinte mask ###-####")
        return getPlacaDoCarro()

if __name__ == "__main__":
    main()