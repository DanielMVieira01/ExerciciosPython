# Aluno: Daniel Martins Vieira
# Lógica de programação

#Verificar se um dado número inteiro é par ou ímpar, positivo ou negativo

x = int(input("Digite um número inteiro:"))

y = x % 2

if  y == 0 and x > 0:
    print("O número",x, "é par e positivo.")

elif y == 0 and x < 0:
    print("O número", x, "é par e negativo.")

elif y != 0 and x > 0:
    print("O número", x, "é impár e positivo.")

elif y != 0 and x < 0:
    print("O número", x, "é impár e negativo.")
