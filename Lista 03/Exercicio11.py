# Aluno: Daniel Martins Vieira
# Lógica de programação

#Implemente um script em python que imprima todos os números múltiplos de 2 ou 3 em um intervalo definido pelo usuário. Este exercício deve ser implementado utilizando o comando for.

x = int(input("Digite o primeiro número: "))
y = int(input("Digite o segundo número: "))
z = x

print("Os múltiplos de 2 do intervalo são: ")
for i in range(x, y+1):
    if x % 2 == 0:
        print(x)
    x += 1
print("Os múltiplos de 3 do intervalo são: ")
for i in range (z, y+1):
    if z % 3 == 0:
        print(z)
    z += 1
