def verificar_par_ou_impar(numero):
    if numero % 2 == 0:
        return "Par"
    else:
        return "Ímpar"

def programa_pares_impares():
    limite = int(input("Digite um número inteiro positivo: "))

    for i in range(1, limite + 1):
        classificacao = verificar_par_ou_impar(i)
        print(f"{i} é {classificacao}")

# Chama a função principal
programa_pares_impares()