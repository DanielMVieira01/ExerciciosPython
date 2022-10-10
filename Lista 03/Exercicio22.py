# Aluno: Daniel Martins Vieira
# Lógica de programação

#Implementar um script em python de modo que sejam impressos os 10 primeiros termos da Série de Fibonacci. Observe que os dois primeiros termos desta série são 1 e 1 e os demais são gerados a partir da soma dos dois termos anteriores.
# Exemplo:
#1 + 1 → 2 (terceiro termo);
#1 + 2 → 3 (quarto termo);
#etc.

x = 0
y = 1

print(" Os 10 primeiros termos da série de fibonacci são: ")
print(y)
for i in range (1, 10):
    c = x + y
    print(c)
    x = y
    y = c