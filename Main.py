class Main:
    pass

from Cliente import Cliente
from Conta import Conta

c1 = Cliente('Enrico','34 98892-6898')

print(c1)
print(c1._nome, ' e ', c1._telefone)

conta = Conta(c1._nome,2526, 0)

print(conta.titular," Numero: ",conta.numero," Saldo: ",conta._saldo)

nome = "Enrico"
print(len(nome))

conta.deposita(100)
conta.saque(99)
conta.extrato()