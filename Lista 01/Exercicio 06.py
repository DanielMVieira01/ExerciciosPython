# Aluno: Daniel Martins Vieira
# Lógica de programação

#Faça um programa em python para ler os dados de um usuário: nome, telefone e endereço. Ao final, o programa deve imprimir na tela um relatório com os dados do usuário.

nome = ("Daniel Martins Vieira")
telefone = ("62 981380069")
endereço = ("Av. Ravena nr 605 - Goiânia / GO.")
x=(input("Digite Sim se desseja ver os dados do usuário:"))
if x == "Sim":
    print("Seguem dados do usuário:")
    print("Nome:",nome)
    print("Telefone:", telefone)
    print("Endereço:", endereço)
else:
    print("Aplicação encerrada.")