# Aluno: Daniel Martins Vieira
# Lógica de programação

# Escreva um programa em python que leia três números inteiros.
# Devemos verificar se com as medidas destes três números conseguimos formar um triângulo.

#Os critérios de verificação são:
#a) Só existe um triângulo se qualquer lado for menor que a soma dos outros dois;
    #Os critérios abaixo se aplicam apenas se existir o triângulo:
        #b) Se os três lados forem iguais, o triângulo é equilátero;
        #c) Se dois lados forem iguais o triângulo é isósceles.
        #d) Se a soma do quadrado de dois lados for igual ao quadrado do terceiro lado,
            #então o triângulo é retângulo.
#O programa deve informar ao usuário se os valores digitados formam ou não um triângulo e também deve informar o tipo do triângulo.

ladoA = int(input("informe o tamaho do lado A:"))
ladoB = int(input("informe o tamaho do lado B:"))
ladoC = int(input("informe o tamaho do lado C:"))

ver1 = ladoA + ladoB
ver2 = ladoB + ladoC
ver3 = ladoA + ladoC

ver4 = ladoA**2 + ladoB**2
ver5 = ladoB**2 + ladoC**2
ver6 = ladoA**2 + ladoC**2

ver7 = ladoA**2
ver8 = ladoB**2
ver9 = ladoC**2

## Verifica se é trinagulo.

if ladoA < ver2:

    if ladoA == ladoB and ladoA == ladoC:
        print("As retas informadas formam um triângulo equilátero")
    elif ladoA == ladoB:
            if ver4 == ver9:
                print("As retas informadas formam um triângulo retangulo isóceles.")
            elif ver5 == ver7:
                print("As retas informadas formam um triângulo retangulo isóceles.")
            elif ver6 == ver8:
                print("As retas informadas formam um triângulo retangulo isóceles.")
            else:
                print("As retas informadas formam um triângulo isóceles.")
    elif ladoA == ladoC:
        if ver4 == ver9:
            print("As retas informadas formam um triângulo retangulo isóceles.")
        elif ver5 == ver7:
            print("As retas informadas formam um triângulo retangulo isóceles.")
        elif ver6 == ver8:
            print("As retas informadas formam um triângulo retangulo isóceles.")
        else:
            print("As retas informadas formam um triângulo isóceles.")
    elif ladoB == ladoC:
        if ver4 == ver9:
            print("As retas informadas formam um triângulo retangulo isóceles.")
        elif ver5 == ver7:
            print("As retas informadas formam um triângulo retangulo isóceles.")
        elif ver6 == ver8:
            print("As retas informadas formam um triângulo retangulo isóceles.")
        else:
            print("As retas informadas formam um triângulo isóceles.")
    else:
        if ver4 == ver9:
            print("As retas informadas formam um triângulo retangulo.")
        elif ver5 == ver7:
            print("As retas informadas formam um triângulo retangulo.")
        elif ver6 == ver8:
            print("As retas informadas formam um triângulo retangulo.")
        else:
            print("As retas informadas formam um triângulo.")

## Verifica se é triangulo.

elif ladoB < ver3:
    if ladoA == ladoB and ladoA == ladoC:
        print("As retas informadas formam um triângulo equilátero")
    elif ladoA == ladoB:
            if ver4 == ver9:
                print("As retas informadas formam um triângulo retangulo isóceles.")
            elif ver5 == ver7:
                print("As retas informadas formam um triângulo retangulo isóceles.")
            elif ver6 == ver8:
                print("As retas informadas formam um triângulo retangulo isóceles.")
            else:
                print("As retas informadas formam um triângulo isóceles.")
    elif ladoA == ladoC:
        if ver4 == ver9:
            print("As retas informadas formam um triângulo retangulo isóceles.")
        elif ver5 == ver7:
            print("As retas informadas formam um triângulo retangulo isóceles.")
        elif ver6 == ver8:
            print("As retas informadas formam um triângulo retangulo isóceles.")
        else:
            print("As retas informadas formam um triângulo isóceles.")
    elif ladoB == ladoC:
        if ver4 == ver9:
            print("As retas informadas formam um triângulo retangulo isóceles.")
        elif ver5 == ver7:
            print("As retas informadas formam um triângulo retangulo isóceles.")
        elif ver6 == ver8:
            print("As retas informadas formam um triângulo retangulo isóceles.")
        else:
            print("As retas informadas formam um triângulo isóceles.")
    else:
        if ver4 == ver9:
            print("As retas informadas formam um triângulo retangulo.")
        elif ver5 == ver7:
            print("As retas informadas formam um triângulo retangulo.")
        elif ver6 == ver8:
            print("As retas informadas formam um triângulo retangulo.")
        else:
            print("As retas informadas formam um triângulo.")
## Verifica se é triangulo

elif ladoC < ver1:
    if ladoA == ladoB and ladoA == ladoC:
        print("As retas informadas formam um triângulo equilátero")
    elif ladoA == ladoB:
            if ver4 == ver9:
                print("As retas informadas formam um triângulo retangulo isóceles.")
            elif ver5 == ver7:
                print("As retas informadas formam um triângulo retangulo isóceles.")
            elif ver6 == ver8:
                print("As retas informadas formam um triângulo retangulo isóceles.")
            else:
                print("As retas informadas formam um triângulo isóceles.")
    elif ladoA == ladoC:
        if ver4 == ver9:
            print("As retas informadas formam um triângulo retangulo isóceles.")
        elif ver5 == ver7:
            print("As retas informadas formam um triângulo retangulo isóceles.")
        elif ver6 == ver8:
            print("As retas informadas formam um triângulo retangulo isóceles.")
        else:
            print("As retas informadas formam um triângulo isóceles.")
    elif ladoB == ladoC:
        if ver4 == ver9:
            print("As retas informadas formam um triângulo retangulo isóceles.")
        elif ver5 == ver7:
            print("As retas informadas formam um triângulo retangulo isóceles.")
        elif ver6 == ver8:
            print("As retas informadas formam um triângulo retangulo isóceles.")
        else:
            print("As retas informadas formam um triângulo isóceles.")
    else:
        if ver4 == ver9:
            print("As retas informadas formam um triângulo retangulo.")
        elif ver5 == ver7:
            print("As retas informadas formam um triângulo retangulo.")
        elif ver6 == ver8:
            print("As retas informadas formam um triângulo retangulo.")
        else:
            print("As retas informadas formam um triângulo.")