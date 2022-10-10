# Aluno: Daniel Martins Vieira
# Lógica de programação

# Escrever um programa para preencher um vetor de 10 posições (inteiros). O conteúdo do vetor é informado pelo usuário. Ao final, o programa deve imprimir todo o conteúdo do vetor.

vetor = []

for i in range(1, 11):
    vetor.append(int(input("Digite o número: ")))

print("O vetor contem os números: ",vetor)