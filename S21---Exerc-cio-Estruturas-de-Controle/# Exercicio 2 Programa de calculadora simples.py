# Função para realizar as operações
def calculadora():
    print("Escolha a operação:")
    print("1. Adição (+)")
    print("2. Subtração (-)")
    print("3. Multiplicação (*)")
    print("4. Divisão (/)")

    # Recebe a escolha do usuário
    operacao = input("Digite o número da operação desejada (1/2/3/4): ")

    # Verifica se a operação é válida
    if operacao in ['1', '2', '3', '4']:
        # Recebe os dois números
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))

        # Realiza a operação correspondente
        if operacao == '1':
            resultado = num1 + num2
            print(f"{num1} + {num2} = {resultado}")
        elif operacao == '2':
            resultado = num1 - num2
            print(f"{num1} - {num2} = {resultado}")
        elif operacao == '3':
            resultado = num1 * num2
            print(f"{num1} * {num2} = {resultado}")
        elif operacao == '4':
            if num2 != 0:
                resultado = num1 / num2
                print(f"{num1} / {num2} = {resultado}")
            else:
                print("Erro: Divisão por zero não é permitida.")
    else:
        print("Operação inválida. Por favor, escolha uma operação válida.")

# Chama a função calculadora
calculadora()
