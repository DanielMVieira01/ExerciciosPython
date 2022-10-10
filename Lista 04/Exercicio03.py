# Aluno: Daniel Martins Vieira
# Lógica de programação

#Escrever um programa para preencher um vetor de 15 posições. O conteúdo do vetor é informado pelo usuário. Ao final, o programa deve imprimir a soma e a média de todo o conteúdo do vetor.

vetor = []
x = 0
for i in range(0, 15):
    vetor.append(eval(input("Digite a informação: ")))
    x += vetor[i]

med = x / 15

print(" A soma do vetor é: ",x)
print(" A média do vetor é: ",med)