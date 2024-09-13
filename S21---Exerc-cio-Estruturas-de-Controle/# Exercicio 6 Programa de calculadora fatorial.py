def calcular_fatorial(numero):
    fatorial = 1
    for i in range(1, numero + 1):
        fatorial *= i
    return fatorial

def programa_fatorial():
    while True:
        numero = int(input("Digite um número inteiro positivo (ou -1 para sair): "))
        
        if numero == -1:
            print("Programa encerrado.")
            break
        elif numero < 0:
            print("Número inválido! Por favor, digite um número inteiro positivo.")
        else:
            fatorial = calcular_fatorial(numero)
            print(f"O fatorial de {numero} é {fatorial}.")

# Chama a função principal
programa_fatorial()
