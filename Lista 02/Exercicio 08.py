# Aluno: Daniel Martins Vieira
# Lógica de programação

#Ler três números inteiros informados pelo usuário e então imprimi-los em ordem crescente.

x= int(input("Digite o primeiro número:"))
y= int(input("Digite o segundo número:"))
z= int(input("Digite o terceiro número:"))

if x < y and x < z:

    if y < z:
        print("A ordem crescente dos números:",x, y, z)
    if y > z:
        print("A ordem crescente dos números:", x, z, y)

if y < x and y < z:

    if x < z:
        print("A ordem crescente dos números:",y, x, z)
    if x > z:
        print("A ordem crescente dos números:", y, z, x)

if z < x and z < y:

    if x < y:
        print("A ordem crescente dos números:",z, x, y)
    else:
        print("A ordem crescente dos números:", z, y, x)