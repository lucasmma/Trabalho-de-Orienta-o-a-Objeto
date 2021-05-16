
class Service:
    veiculos = []
    acessos = []
    pessoasFisicas = []
    def __init__(self):
        return 

    def cadastrarVeiculo(self, Veiculo):
        self.veiculos.append(Veiculo)
        return

    def cadastrarPessoaFisica(self, PessoaFisica):
        self.pessoasFisicas.append(PessoaFisica)
        return

    def cadastrarAcesso(self,Acesso):
        self.acessos.append(Acesso)
        return


    def getVeiculo(self, placa):
        for veiculo in self.veiculos:
            if(veiculo.numero_da_placa == placa):
                return veiculo

        return None

    def getPessoaFisica(self, cnh):
        for pessoafisica in self.veiculos:
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