# Aluno: Daniel Martins Vieira
# Lógica de programação

# Construir um programa que leia um número inteiro e positivo informado pelo usuário. O programa deve verificar se o número informado pelo usuário é primo ou não. Um número primo é aquele que é divisível apenas por 1 e por ele mesmo. Este exercício deve ser implementado utilizando o comando while.

x = int(input("Digite um número inteiro e positivo: "))
y = 1
z = 0

while y <= x:
    if x % y == 0:
        z += 1
    y += 1
if z == 2:
    print("O número é primo.")
else:
    print("O número não é primo.")

