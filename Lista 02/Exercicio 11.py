# Aluno: Daniel Martins Vieira
# Lógica de programação

#Construir um programa para calcular o IMC (Índice de Massa Corpórea) de uma pessoa, considerando a seguinte tabela:

peso = eval(input("Informe seu peso: "))
altura = eval(input("Informe sua altura:"))

imc = peso / (altura**2)

print(imc)

if imc < 19.1:
    print("Você está abaixo do peso.")
elif imc >= 19.1 and imc <= 25.8:
    print("Você está no peso ideal.")
elif imc > 25.8 and imc < 27.3:
    print("Você está um pouco acima do peso.")
elif imc >= 27.3 and imc <= 32.3:
    print("Você está muito acima do peso.")
elif imc > 32.3:
    print("Você está obesso.")