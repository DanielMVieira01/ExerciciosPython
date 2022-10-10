# Aluno: Daniel Martins Vieira
# Lógica de programação

#Implementar um script em python que imprima os números pares entre 100 e 150. Este exercício deve ser implementado utilizando o comando while.

x = 100
print("Os números pares entre 100 e 150 são:")

while x <= 150:
    if x % 2 == 0:
        print(x)
    x += 1