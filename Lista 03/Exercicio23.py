# Aluno: Daniel Martins Vieira
# Lógica de programação

# 23. Implemente um script em python para ler 5 números inteiros informados pelo usuário. Ao final, seu programa deve imprimir a média aritmética destes números. Este exercício deve ser implementado utilizando o comando for.

x = 0
for i in range (1, 6):
    y = int(input("Digite um número: "))

    x += y
med = x // 5
print("A média dos números é: ",med)
