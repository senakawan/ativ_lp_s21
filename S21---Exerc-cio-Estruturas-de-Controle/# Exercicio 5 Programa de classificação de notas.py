def classificar_aluno(media):
    if media >= 7:
        return "Aprovado"
    elif 5 <= media < 7:
        return "Recuperação"
    else:
        return "Reprovado"

def programa_notas():
    continuar = True
    
    while continuar:
        # Solicita as notas
        nota1 = float(input("Digite a primeira nota do aluno: "))
        nota2 = float(input("Digite a segunda nota do aluno: "))
        
        # Calcula a média
        media = (nota1 + nota2) / 2
        
        # Classifica o aluno
        classificacao = classificar_aluno(media)
        print(f"A média do aluno é {media:.2f}. O aluno está {classificacao}.")
        
        # Pergunta se o usuário quer continuar
        resposta = input("Deseja inserir as notas de outro aluno? (s/n): ")
        if resposta.lower() != 's':
            continuar = False
    
    print("Programa encerrado.")

# Chama a função principal
programa_notas()
