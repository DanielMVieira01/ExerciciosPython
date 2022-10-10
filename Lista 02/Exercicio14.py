# Aluno: Daniel Martins Vieira
# Lógica de programação

# O exercício em questão consiste em resolver o problema do troco em um estabelecimento comercial. No Brasil, temos moedas de 1 real, 50 centavos, 25 centavos, 10 centavos, 5 centavos e 1 centavo. O problema do troco consiste em pagar um troco com a menor quantidade possível de moedas. Por exemplo, para um troco de R$ 2,78, a solução ótima seria: 2 moedas de 1 real, 1 moeda de 50 centavos, 1 moeda de 25 centavos e 3 moedas de 1 centavo (total de 7 moedas). É possível elaborar um programa em python para resolver este problema? Em caso afirmativo, escreva um script em python para a resolução da questão.

from decimal import Decimal

troco = float(input("Informe o valor do troco:"))
troco = str(troco)
trocoInt = int(Decimal(troco) * 100)

print(trocoInt)

moeda1 = trocoInt // 100
restoMoeda1 = trocoInt % 100

moeda50 = restoMoeda1 // 50
restoMoeda50 = restoMoeda1 % 50

moeda25 = restoMoeda50 // 25
restoMoeda25 = restoMoeda50 % 25

moeda10 = restoMoeda25 // 10
restoMoeda10 = restoMoeda25 % 10

moeda5 = restoMoeda10 // 5
restoMoeda5 = restoMoeda10 % 5

moeda01 = restoMoeda5 // 1
restoMoeda01 = restoMoeda5 % 1

print("O Total de moeda(s) 1.00 é. ", moeda1)
print("O Total de moeda(s) 0.50 é. ", moeda50)
print("O Total de moeda(s) 0.25 é. ", moeda25)
print("O Total de moeda(s) 0.10 é. ", moeda10)
print("O Total de moeda(s) 0.05 é. ", moeda5)
print("O Total de moeda(s) 0.01 é. ", moeda01)