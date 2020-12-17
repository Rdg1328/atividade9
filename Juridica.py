from Pessoa import Pessoa

class Juridica(Pessoa):
    def __init__(self, cod, nome, endereco, telefone, cnpj, insEstadual, quantFuncionarios):
        Pessoa.__init__(self, cod, nome, endereco, telefone)
        self.__cnpj = cnpj
        self.__insEstadual = insEstadual
        self.quantFuncionarios = quantFuncionarios

    def imprimeCNPJ(self):
        print(self.__cnpj)

    def __emitirNota(self):
        print(self.__insEstadual)

    def getNotaFiscal(self):
        return (self.__emitirNota())