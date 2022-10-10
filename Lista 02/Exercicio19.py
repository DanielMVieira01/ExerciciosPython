# Aluno: Daniel Martins Vieira
# Lógica de programação

# Faça um algoritmo para ler: número da conta do cliente, saldo, débito e crédito. Após, calcular e escrever o saldo atual (saldo atual = saldo - débito + crédito). Também testar se saldo atual for maior ou igual a zero escrever a mensagem 'Saldo Positivo', senão escrever a mensagem 'Saldo Negativo'.

contaCliente = eval(input("Digite o número da sua conta: "))
saldoAnterior = float(input("Digite o saldo anterior: "))
debito = float(input("Informe o valor de débito: "))
credito = float(input("Informe o valor de crédito: "))

saldoAtual = (saldoAnterior - debito + credito )

if saldoAtual >= 0:
    print("Saldo Positivo no valor de: R$",saldoAtual)
else:
    print("Saldo Negativo no valor de: R$", saldoAtual)