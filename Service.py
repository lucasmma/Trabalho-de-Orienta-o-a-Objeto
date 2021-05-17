

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
   
    def getAcesso(self, id_acesso):
        for acesso in self.acessos:
            if(acesso.id_acesso == id_acesso):
                return acesso

        return None

    def listarVeiculos(self):
        for veiculo in self.veiculos:
            veiculo.printClass()

        return 

    def listarPessoasFisicas(self):
        for pessoasfisica in self.pessoasFisicas:
            pessoasfisica.printClass()

        return 


    def listarAcessos(self):
        for pessoasfisica in self.pessoasFisicas:
            pessoasfisica.printClass()

        return 