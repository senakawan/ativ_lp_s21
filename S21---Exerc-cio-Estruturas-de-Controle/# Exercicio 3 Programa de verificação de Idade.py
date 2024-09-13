def verificar_idade(idade):
    if idade < 18:
        return "Menor de idade"
    elif 18 <= idade < 60:
        return "Maior de Idade"
    else:
        return "Idoso"

def programa_idade():
    while True:
        # Recebe a idade do usuário
        idade = int(input("Digite a idade da pessoa (ou -1 para parar): "))
        
        if idade == -1:
            break  # Sai do laço se o usuário digitar -1
        
        # Verifica e exibe a categoria da pessoa com base na idade
        categoria = verificar_idade(idade)
        print(f"A pessoa é: {categoria}")

# Chama a função principal
programa_idade()
