# Aluno: Daniel Martins Vieira
# Lógica de programação

#Escrever um programa para preencher um vetor de 08 posições. O conteúdo do vetor é informado pelo usuário. Ao final, o programa deve imprimir apenas os números pares informados pelo usuário.

vetor = []
par = []
for i in range(0, 8):
    vetor.append(eval(input("Digite um número: ")))
    if vetor[i] % 2 == 0:
        par.append(vetor[i])
print("Os pares são: ")
print(par)