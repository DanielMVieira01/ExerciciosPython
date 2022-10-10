# Aluno: Daniel Martins Vieira
# Lógica de programação

#Um número é quadrado perfeito quando tem um número inteiro como raiz quadrada. Isso posto, implemente um script em python para que o usuário digite vários números e o programa verifica se este número é ou não um quadrado perfeito. O programa se encerra quando o usuário digita um número menor ou igual a 0.

import math
x = 1
while x >= 1:
    y = int(input("Digite um número: "))
    if y > 0:
        z = math.sqrt(y)
        a = int(z)
        if a * a == y:
            print("O número é um quadrado perfeito!")
        else:
            print("O número não é um quadrado perfeito.")
    elif y <= 0:
        print("O Número não é válido")

        break