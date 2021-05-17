

class Service:
    def __init__(self):
        self.veiculos = []
        self.acessos = []
        self.pessoasFisicas = []
        return 

    def cadastrarVeiculo(self, veiculo):
        self.veiculos.append(veiculo)
        return

    def cadastrarPessoaFisica(self, pessoafisica):
        self.pessoasFisicas.append(pessoafisica)
        return

    def cadastrarAcesso(self, acesso):
        self.acessos.append(acesso)
        return

    def updateVeiculo(self, veiculo):
        for i in range(0, len(self.veiculos)):
            if(self.veiculos[i].numero_da_placa == veiculo.numero_da_placa):
                self.veiculos[i] = veiculo
        return

    def getVeiculo(self, placa):
        for veiculo in self.veiculos:
            if(veiculo.numero_da_placa == placa):
                return veiculo

        return None

    def getPessoaFisica(self, cnh):
        for pessoafisica in self.pessoasFisicas:
            if(pessoafisica.cnh == cnh):
                return pessoafisica

        return None
   
    def getAcesso(self, numerodaplaca):
        for acesso in self.acessos:
            if((numerodaplaca in acesso.id_acesso) and (acesso.hora_saida == None)):
                return acesso

        return None

    def listarVeiculos(self):
        for index in range(0, len(self.veiculos)):
            print("Veículo " + str(index))
            self.veiculos[index].printClass()

        return 

    def listarPessoasFisicas(self):
        for index in range(0, len(self.pessoasFisicas)):
            print("Pessoa física " + str(index))
            self.pessoasFisicas[index].printClass()

        return 


    def listarAcessos(self):
        for index in range(0, len(self.acessos)):
            print("Acesso " + str(index))
            self.acessos[index].printClass()

        return 