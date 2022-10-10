# Aluno: Daniel Martins Vieira
# Lógica de programação

# Construir um programa em python que leia um número inteiro e positivo informado pelo usuário. O programa deve imprimir todos os números pares entre 0 e o numero informado pelo usuário. Depois, o programa deve imprimir todos os número ímpares entre 0 e o numero informado pelo usuário. Este exercício deve ser implementado utilizando o comando for.

x = int(input("Digite um número inteiro e positivo: "))

print("Os números abaixo são par:")
for i in range(0, x+1, 2):
    print(i)
print("Os números abaixo são ímpar:")
for c in range(1, x+1, 2):
    print(c)