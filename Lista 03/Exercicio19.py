# Aluno: Daniel Martins Vieira
# Lógica de programação

#Implemente um script em python para calcular o MMC (mínimo múltiplo comum) entre dois números informados pelo usuário.

x = int(input("Digite o número 1: "))
y = int(input("Digite o número 2: "))

if x > y:
    maior = x
else:
     maior = y
while True:

    if maior % x == 0 and maior % y ==0:
        print("O MMC é: ",maior)
        break
    else:
        maior += 1

