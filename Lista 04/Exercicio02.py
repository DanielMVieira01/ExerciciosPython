# Aluno: Daniel Martins Vieira
# Lógica de programação

#Escrever um programa para preencher um vetor de 10 posições. O conteúdo do vetor é informado pelo usuário. Ao final, o programa deve imprimir todo o conteúdo do vetor em ordem inversa.

vetor = []
x = 9

for i in range(1, 11):
    vetor.append(input("Digite a informação: "))
print("O vetor contem os números:")
while x >= 0:
    print(vetor[x])
    x -= 1