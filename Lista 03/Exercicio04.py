# Aluno: Daniel Martins Vieira
# Lógica de programação

#Construir um programa em python que leia um número inteiro e positivo informado pelo usuário. O programa deve imprimir todos os números pares entre 0 e o numero informado pelo usuário. Depois, o programa deve imprimir todos os número ímpares entre 0 e o numero informado pelo usuário. Este exercício deve ser implementado utilizando o comando while.

x = int(input("Digite um número inteiro e positivo: "))
y = x
print("Os números são pares:")
while x >= 0:
    if x % 2 == 0:
        print(x)
    x -= 1
print("O números são impares:")
while y >= 0:
    if y % 2 > 0:
        print(y)
    y -= 1
