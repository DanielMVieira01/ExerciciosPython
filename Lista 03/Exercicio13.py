# Aluno: Daniel Martins Vieira
# Lógica de programação

#Implemente um script em python de modo que o usuário informe um número e o programa imprima como resultado todos os divisores daquele número. Este exercício deve ser implementado utilizando o comando for.

x = int(input("Digite o número: "))
y = 0
print("Os divisores dos números são: ")
for i in range(1, x+1):
    if x % i == 0:
        print(i)
    y += 1