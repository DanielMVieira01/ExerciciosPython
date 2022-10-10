# Aluno: Daniel Martins Vieira
# Lógica de programação

#Em matemática, a Sucessão de Fibonacci (também Sequência de Fibonacci), é uma sequência de números inteiros, começando normalmente por 0 e 1, na qual, cada termo subsequente (número de Fibonacci) corresponde a soma dos dois anteriores.

import math

x = int(input("digite o valor:"))

fibo = int(1/math.sqrt(5)* ( ((1+math.sqrt(5))/2)**x - ((1-math.sqrt(5))/2)**x ))

print("O termo é:",fibo)
