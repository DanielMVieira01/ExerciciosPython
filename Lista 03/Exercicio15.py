# Aluno: Daniel Martins Vieira
# Lógica de programação

# Implementar um script em python para que o usuário informe 10 números positivos e imprima o quadrado destes números. Para cada entrada o programa deverá verificar se o número é negativo. Caso seja, o número não deve ser aceito, ou seja, deve haver uma proteção para a entrada de dados.

x = 1
while x <= 10:
    y = int(input("Digite um número: "))
    if y >= 0:
        z = y ** 2
        print("O quadrado do número é: ",z)
        x += 1
    elif y < 0:
        print("O número é negativo!")