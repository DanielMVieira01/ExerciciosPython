# Aluno: Daniel Martins Vieira
# Lógica de programação

#Escrever um programa para preencher um vetor de 10 posições com itens informados pelo usuário. Ao final, seu programa deve informar quantos e quais itens são string e quantos e quais itens são numéricos.

vetor = []
string = []
somaStr = 0
numer = []
somaNum = 0
for i in range(0, 3):
    vetor.append(input("Digite : "))
    if type(vetor[i]) is str:
        string.append(vetor[i])
        somaStr += 1
print(string)
print(somaStr)
print(numer)
print(somaNum)
print(type(vetor[0]))