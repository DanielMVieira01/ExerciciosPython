# Aluno: Daniel Martins Vieira
# Lógica de programação

#Implemente um script em python de modo que o usuário informe um número e o programa imprima como resultado todos os divisores daquele número. Este exercício deve ser implementado utilizando o comando while.

x = int(input("Digite o número: "))
y = 1
print("Os divisores dos números são: ")
while y <= x:
    if x % y == 0:
        print(y)
    y += 1