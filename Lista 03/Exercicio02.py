# Aluno: Daniel Martins Vieira
# Lógica de programação

# A Sucessão de Fibonacci é uma sequência de números inteiros, começando normalmente por 0 e 1, na qual, cada termo subsequente (numero de Fibonacci) corresponde a soma dos dois anteriores.Desta forma, os números de Fibonacci são os números que compõem a seguinte sequência: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, … Escreva um programa que solicite ao usuário informar um número que representa o n-esimo termo da sequencia de Fibonacci.
#Exemplo:
#- o 5º termo da sequencia é: 3
#- o 10º termo da sequencia é: 34
#- etc
# Ao informar o n-esimo termo da sequencia, o programa deve imprimir todos os termos de Fibonacci até o n-esimo termo.

x = int(input("digite o valor:"))
y = x-2
a = 0
b = 1
c = a + b
print(a)
print(b)
while  y > 0:
    print(c)
    a = b
    b = c
    c = a + b
    y -= 1


