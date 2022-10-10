# Aluno: Daniel Martins Vieira
# Lógica de programação

# Escreva um programa em python para armazenar dois valores inteiros informados pelo usuário, por exemplo, nas variáveis x e y. Deve-se realizar a troca dos valores das variáveis e, por fim, deve-se imprimir os valores finais das variáveis.

x = int(input("Digite o valor de x:"))
y = int(input("Digite o valor de y:"))

a = x
x = y
y = a

print("O valor final de x é:",x)
print("O valor final de y é:",y)