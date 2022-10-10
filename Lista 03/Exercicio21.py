# Aluno: Daniel Martins Vieira
# Lógica de programação

#Sabe-se que a Unidade Lógica e Aritmética (ULA) calcula o produto através de somas sucessivas. Neste sentido, implemente um script em python para calcular o produto de dois números inteiros informados pelo usuário. Suponha que os números lidos sejam positivos e que o multiplicando seja menor que o multiplicador.

x = int(input("Digite o número 1: "))
y = int(input("Digite o número 2: "))

if x > y:
    multiplicador = x
    multiplicando = y
else:
     multiplicador = y
     multiplicando = x
produto = 0
for i in range(1, multiplicador +1):
    produto += multiplicando

print("O produto dos números é: ",produto)

