class Main:
    pass

from Cliente import Cliente
from Conta import Conta

c1 = Cliente('Enrico','34 98892-6898')

print(c1)
print(c1.nome, ' e ', c1.telefone)

conta = Conta(c1.nome,2526, 0)

print(conta.titular," Numero: ",conta.numero," Saldo: ",conta.saldo)