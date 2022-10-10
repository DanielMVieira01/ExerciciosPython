# Aluno: Daniel Martins Vieira
# Lógica de programação

#Implemente um script em python para calcular o MDC (máximo divisor comum) entre dois números informados pelo usuário.

x = int(input("Digite o número 1: "))
y = int(input("Digite o número 2: "))

if x > y:
    dividendo = x
    divisor = y
else:
     dividendo = y
     divisor = x

cociente = dividendo // divisor
resto = dividendo % divisor
while resto != 0:
    resto = dividendo % divisor
    if resto > 0:
        dividendo = divisor
        divisor = resto
        mdc = resto
print("O MDC é:",mdc)

