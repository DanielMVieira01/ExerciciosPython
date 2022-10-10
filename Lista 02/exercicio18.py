# Aluno: Daniel Martins Vieira
# Lógica de programação

# Faça um algoritmo para ler um número que é um código de usuário. Caso este código seja diferente de um código armazenado internamente no algoritmo (igual a 1234) deve ser apresentada a mensagem ‘Usuário inválido!’.
# Caso o Código seja correto, deve ser lido outro valor que é a senha. Se esta senha estiver incorreta (a certa é 9999) deve ser mostrada a mensagem ‘senha incorreta’. Caso a senha esteja correta, deve ser mostrada a mensagem ‘Acesso permitido’.

codigoUsua = 123456
senha = 0000

codUser1 = int(input("Código de usuário: "))
if codUser1 == codigoUsua:
    senha1 =  int(input("Senha: "))
    if senha1 == senha:
            print("Acesso liberado.")
    else:
            print("Senha incorreta.")
else:
    print("Usuário Inválido.")



