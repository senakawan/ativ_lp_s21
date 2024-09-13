# Programa de validação de senha

# Senha correta
senha_correta = "sccp1910"
# Loop para solicitar a senha até que o usuário digite a correta
while True:
    # Solicita ao usuário que insira a senha
    senha = input("Digite a senha: ")
    
    # Verifica se a senha inserida é a correta
    if senha == senha_correta:
        print("Acesso permitido")
        break  # Sai do loop quando a senha está correta
    else:
        print("Senha incorreta")
