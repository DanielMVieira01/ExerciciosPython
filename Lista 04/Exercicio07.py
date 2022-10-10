# Aluno: Daniel Martins Vieira
# Lógica de programação

#Escrever um programa para preencher um vetor de 10 posições. O conteúdo do vetor é informado pelo usuário. Ao final, o programa deve imprimir apenas os números de posição impar informados pelo usuário.

vetor = []

for i in range(0, 10):
    vetor.append(eval(input("Digite um número: ")))
print("Os números nas posições ímpares são: ")
for i in range (0, 12):
    if i % 2 > 0:
        print(vetor[i])