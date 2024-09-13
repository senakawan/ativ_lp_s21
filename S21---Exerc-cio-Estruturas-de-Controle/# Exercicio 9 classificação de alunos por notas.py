def classificar_aluno(nota):
    return "Aprovado" if nota >= 7 else "Reprovado"

def programa_classificacao():
    notas = []
    nomes = []

    # Coleta os dados dos alunos
    for i in range(5):
        nome = input(f"Digite o nome do aluno {i+1}: ")
        nota = float(input(f"Digite a nota do aluno {i+1}: "))
        nomes.append(nome)
        notas.append(nota)

    # Calcula a média da turma
    media = sum(notas) / len(notas)
    
    print(f"\nMédia da turma: {media:.2f}")
    
    # Classifica e exibe o status de cada aluno
    for nome, nota in zip(nomes, notas):
        status = classificar_aluno(nota)
        print(f"{nome} - Nota: {nota:.2f} - {status}")

# Chama a função principal
programa_classificacao()
