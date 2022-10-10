# Aluno: Daniel Martins Vieira
# Lógica de programação

#Faça um programa em python para ler dois números inteiros informados pelo usuário. Ao final o programa deve imprimir um relatório com o seguinte formato:- dividendo: - divisor: - quociente: - resto:

dividendo=int(input("Digite o número dessejado:"))
divisor=int(input("Digite o número dessejado:"))
resto= dividendo % divisor
quociente= dividendo // divisor
print("As propriedadades da divisão são:")
print("O dividendo é:",dividendo)
print("O divisor é:",divisor)
print("O quociente é:",quociente)
print("O resto é:",resto)
