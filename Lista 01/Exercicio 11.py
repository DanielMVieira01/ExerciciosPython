# Aluno: Daniel Martins Vieira
# Lógica de programação

#Faça um programa em python para ler dois valores numéricos informados pelo usuário que representam as dimensões da base e altura de um retângulo. Ao final, seu programa deve imprimir um relatório informando os valores repassados pelo usuário e também o valor da área e perímetro deste retângulo.

base= float(input("Digite o tamanho em metros da base do retângulo:"))
altura= float(input("Digite o tamanho em metros da altura do retângulo:"))

area = base * altura
perimetro = 2*base + 2*altura

print("O valor da base do retângulo é:",base,"m")
print("O valor da altura do retângulo é:",altura,"m")
print("O valor da área do retângulo é:",area,"m²")
print("O valor do perímetro do retângulo é:",perimetro,"m")