# Aluno: Daniel Martins Vieira
# Lógica de programação

#5. Ler três números inteiros informados pelo usuário e então imprimir o maior número.

x= int(input("Digite o primeiro número:"))
y= int(input("Digite o segundo número:"))
z= int(input("Digite o terceiro número:"))

if x > y and x > z:
    print("O número", x, "é maior!")
elif y > x and y > z:
    print("O número", y, "é maior!")
else:
    print("O número", z, "é maior!")