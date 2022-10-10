# Aluno: Daniel Martins Vieira
# Lógica de programação

#Implementar um script em python que leia vários números inteiros informados pelo usuário e informe o fatorial de cada número. O programa se encerra quando o usuário digita um valor menor do que 1.

x = 1
while x >= 1:
    z = int(input("Digite um número: "))
    y = z
    if z >= 1:
        print("O fatorial do número é: ")
        for i in range(1, z):
            y *= i
        print(y)
    elif z < 1:
        print("O Número não é válido")
        break

