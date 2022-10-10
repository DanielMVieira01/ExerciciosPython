# Aluno: Daniel Martins Vieira
# Lógica de programação

#Faça um algoritmo para ler: quantidade atual em estoque, quantidade máxima em estoque e quantidade mínima em estoque de um produto. Calcular e escrever a quantidade média ((quantidade média = quantidade máxima + quantidade mínima)/2). Se a quantidade em estoque for maior ou igual a quantidade média escrever a mensagem 'Não efetuar compra', senão escrever a mensagem 'Efetuar compra'.

qtdAtual = eval(input("Informe a quantidade atual do produto: "))
qtdMaxima = eval(input("Informe a quantidade máxima do produto em estoque: "))
qtdMinima = eval(input("Informe a quantidade mínima do produto em estoque: "))

qtdMedia = ((qtdMaxima + qtdMinima) / 2)

if qtdAtual >= qtdMedia:
    print("Não efetuar compra.")
else:
    print("Efetuar compra.")