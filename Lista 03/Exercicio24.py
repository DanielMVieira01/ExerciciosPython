# Aluno: Daniel Martins Vieira
# Lógica de programação

# 23. Implemente um script em python para ler 5 números inteiros informados pelo usuário. Ao final, seu programa deve imprimir a média aritmética destes números. Este exercício deve ser implementado utilizando o comando while.

x = 0
y = 0
while y != 5:
    a = int(input("Digite um número: "))

    x += a
    y +=1
med = x // 5
print("A média dos números é: ",med)