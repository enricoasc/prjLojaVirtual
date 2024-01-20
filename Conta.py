class Conta:
    def __init__(self, titular, numero, saldo ):
        self._saldo = 0
        self.numero = numero
        self.titular = titular

    def get_saldo(self):
        return self._saldo

    def set_saldo(self,saldo):
        if (saldo < 0):
            print('O saldo não pode ser negativo')
        else:
            self._saldo = saldo

    def saque(self,valor):
        if(self._saldo>=valor):
            self._saldo-=valor
            print('Saque realizado com sucesso :..')
        else:
            print('Saque inuficiente :..')

    def deposita(self,valor):
        self._saldo+=valor


    def extrato(self):
        print("Cliente: ",self.titular, " Saldo atual: ", self.get_saldo() )