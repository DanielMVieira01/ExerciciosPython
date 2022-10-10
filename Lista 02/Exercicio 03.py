# Aluno: Daniel Martins Vieira
# Lógica de programação

#Ler dois números inteiros informados pelo usuário e então imprimi-los em ordem decrescente.

x= int(input("Digite o primeiro número:"))
y= int(input("Digite o segundo número:"))

if x > y:
    print("Os números digitados em ordem decrescente são:",x, y)
elif y > x:
    print("Os números digitados em ordem decrescente são:",y, x)