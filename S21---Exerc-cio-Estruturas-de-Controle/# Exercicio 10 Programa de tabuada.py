def exibir_tabuada(numero):
    print(f"\nTabuada do {numero}:")
    for i in range(1, 11):
        resultado = numero * i
        print(f"{numero} x {i} = {resultado}")

def programa_tabuada():
    while True:
        try:
            numero = int(input("Digite um número inteiro para exibir a tabuada (ou -1 para sair): "))
            
            if numero == -1:
                print("Programa encerrado.")
                break
            elif numero < 0:
                print("Por favor, insira um número inteiro positivo ou 0 para sair.")
            else:
                exibir_tabuada(numero)
        except ValueError:
            print("Entrada inválida! Por favor, insira um número inteiro.")

# Chama a função principal
programa_tabuada()
