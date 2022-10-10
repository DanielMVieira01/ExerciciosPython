# Aluno: Daniel Martins Vieira
# Lógica de programação

#Implemente um script em python para verificar se um número informado pelo usuário é ou não triangular. Um número triangular é aquele formado pelo produto de três números consecutivos. Por exemplo: 24 = 2 x 3 x 4.

x = int(input("Digite o número: "))
y = 1
z = 2
for i in range(1, x+1):
    y += 1
    z += 1
    d = i * y * z
    if d == x:
        print("O número é triangular.")
        break
    elif i == x:
        print("O número não é triangular:")