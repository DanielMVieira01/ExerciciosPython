# Aluno: Daniel Martins Vieira
# Lógica de programação

#Ler dois números inteiros informados pelo usuário e então imprimir o menor

x= int(input("Digite o primeiro número:"))
y= int(input("Digite o segundo número:"))

if x > y:
    print("O número ",x, "é maior que ",y)
elif y > x:
    print("O número ", y, "é maior que ",x)
