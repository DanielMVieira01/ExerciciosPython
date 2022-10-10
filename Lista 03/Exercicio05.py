# Aluno: Daniel Martins Vieira
# Lógica de programação

# Construir um programa que leia um número inteiro e positivo informado pelo usuário. O programa deve verificar se o número informado pelo usuário é primo ou não. Um número primo é aquele que é divisível apenas por 1 e por ele mesmo.Este exercício deve ser implementado utilizando o comando for.

x = int(input("Digite um número inteiro e positivo: "))
y = 0
for i in range(1, x+1):
    if x % i == 0:
        y += 1
if y == 2:
    print("O número é primo.")
else:
    print("O número não é primo.")
