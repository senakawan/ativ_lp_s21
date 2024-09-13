def calcular_imc(peso, altura):
    return peso / (altura ** 2)

def classificar_imc(imc):
    if imc < 18.5:
        return "Abaixo do peso"
    elif 18.5 <= imc < 24.9:
        return "Peso normal"
    elif 25 <= imc < 29.9:
        return "Acima do peso"
    else:
        return "Obesidade"

def programa_imc():
    peso = float(input("Digite o seu peso em kg: "))
    altura = float(input("Digite a sua altura em metros: "))
    
    imc = calcular_imc(peso, altura)
    classificacao = classificar_imc(imc)
    
    print(f"Seu IMC é {imc:.2f}. Classificação: {classificacao}")

# Chama a função principal
programa_imc()
