# Aluno: Daniel Martins Vieira
# Lógica de programação

#Implementar um script em python que imprima todos os números entre 1 e 50. Ao final, o programa também deve imprimir o somatório destes números. Este exercício deve ser implementado utilizando o comando while.

x = 1
y = 0
while x <= 50:
    print(x)
    y += x
    x += 1
print("O somatório dos números entre 1 e 50 é:",y)