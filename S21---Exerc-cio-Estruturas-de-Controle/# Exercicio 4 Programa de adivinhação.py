import random

def jogo_adivinhar_numero():
    numero_secreto = random.randint(1, 20)  # Gera um número aleatório entre 1 e 20
    tentativas = 0

    print("Tente adivinhar o número entre 1 e 20!")

    while True:
        palpite = int(input("Digite seu palpite: "))
        tentativas += 1
        
        if palpite < numero_secreto:
            print("Muito baixo! Tente novamente.")
        elif palpite > numero_secreto:
            print("Muito alto! Tente novamente.")
        else:
            print(f"Parabéns! Você acertou o número {numero_secreto} em {tentativas} tentativas.")
            break

# Chama o jogo
jogo_adivinhar_numero()
