# Aluno: Daniel Martins Vieira
# Lógica de programação

# Chama-se ano bissexto o ano ao qual é acrescentado um dia extra, ficando ele com 366 dias, um dia a mais do que os anos normais de 365 dias, ocorrendo a cada quatro anos (exceto anos múltiplos de 100 que não são múltiplos de 400). Isto é feito com o objetivo de manter o calendário anual ajustado com a translação da Terra e com os eventos sazonais relacionados às estações do ano. O último ano bissexto foi 2020 e o próximo será 2024. Fazer um programa que peça ao usuário para digitar um valor inteiro correspondente a um ano qualquer. O programa deve informar ao usuário se o ano é bissexto ou não. Informar qual foi o ano bissexto anterior e o próximo.

ano =  int(input("Informe o ano:"))
bissA = 0
bissP = 0
ano1 = ano

if ano % 4 == 0:
    if ano % 100 != 0:
        print("O ano é bissexto.")
    elif ano % 400 == 0:
        print("O ano é bissexto.")
    else:
        print("O ano não é bissexto")

while bissA == 0:
    ano -= 1
    if ano % 4 == 0:
        if ano % 100 != 0:
            bissA = 1
            print("O ano bissexto anterior é:", ano)
        elif ano % 400 == 0:
            bissA = 1
            print("O ano bissexto anterior é:", ano)
while bissP == 0:
    ano1 += 1
    if ano1 % 4 == 0:
        if ano1 % 100 != 0:
            bissP = 1
            print("O ano bissexto posterior é:", ano1)
        elif ano1 % 400 == 0:
            bissP = 1
            print("O ano bissexto posterior é:", ano1)
