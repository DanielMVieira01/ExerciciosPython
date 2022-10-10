# Aluno: Daniel Martins Vieira
# Lógica de programação

#Escrever um programa para preencher um vetor de 10 posições. O conteúdo do vetor é informado pelo usuário. Ao final, o programa deve imprimir apenas os números impares informados pelo usuário.

vetor = []
impar = []
for i in range(0, 8):
    vetor.append(eval(input("Digite um número: ")))
    if vetor[i] % 2 > 0:
        impar.append(vetor[i])
print("Os ímpares são: ")
print(impar)