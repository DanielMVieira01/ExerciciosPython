# Aluno: Daniel Martins Vieira
# Lógica de programação

#Faça um programa em python para ler um número inteiro informado pelo usuário. Ao final o programa deve informar na tela o resto da divisão deste número por 2, por 3 e por 5.

ab=int(input("Digite o número inteiro desejado:"))

x= ab % 2
z= ab % 3
y= ab % 5

print("O valor do resto da divisão por 2:",x)
print("O valor do resto da divisão por 3:",z)
print("O valor do resto da divisão por 5:",y)