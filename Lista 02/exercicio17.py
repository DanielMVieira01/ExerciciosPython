# Aluno: Daniel Martins Vieira
# Lógica de programação

#Escreva um algoritmo que leia as idades de 2 homens e de 2 mulheres (considere que as idades dos homens serão sempre diferentes entre si, bem como as das mulheres). Calcule e escreva a soma das idades do homem mais velho com a mulher mais nova, e o produto das idades do homem mais novo com a mulher mais velha.

hom1 = int(input("Digite a idade do homen 1: "))
hom2 = int(input("Digite a idade do homen 2: "))
mulh1 = int(input("Digite a idade da mulher 1: "))
mulh2 = int(input("Digite a idade da mulher 2: "))

if hom1 > hom2:
    if mulh1 > mulh2:
        a1 = hom1 + mulh2
        a2 = hom2 * mulh1
else:
    if mulh1 > mulh2:
        a1 = hom2 + mulh2
        a2 = hom1 * mulh1
    else:
        a1 = hom2 + mulh1
        a2 = hom1 * mulh2
print("Cenário 1: A soma da idade do homem mais velho com a mulher mais nova é ",a1)
print("Cenário 2: O produto das idades do homem mais novo com a mulher mais velha é ",a2)

