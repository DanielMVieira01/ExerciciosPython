# Aluno: Daniel Martins Vieira
# Lógica de programação

# Ler três números inteiros informados pelo usuário e então imprimir o menor número.

x= int(input("Digite o primeiro número:"))
y= int(input("Digite o segundo número:"))
z= int(input("Digite o terceiro número:"))

if x < y and x < z:
    print("O número", x, "é menor!")
elif y < x and y < z:
    print("O número", y, "é menor!")
else:
    print("O número", z, "é menor!")