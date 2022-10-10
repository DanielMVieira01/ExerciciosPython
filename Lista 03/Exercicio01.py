# Aluno: Daniel Martins Vieira
# Lógica de programação

# O que é o fatorial de um número n? Exemplo: 5! = 5 * 4 * 3 * 2 * 1 = 120. Isso posto, escreva um programa em python que solicite ao usuário informar um número inteiro. O programa deve calcular o valor do fatorial e imprimir o resultado para o usuário.

x = int(input("Digite o número: "))
y = x

while x > 1:
    y *= (x-1)
    x -= 1

print("O número digitado é: ",y)



