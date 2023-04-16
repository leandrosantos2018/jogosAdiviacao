import random

def jogar():
    print("********************************")
    print("Bem-vindo ao jogo de Adivinhação")
    print("********************************")

    #gerando numero aleatori com biblioteca Random
    numero_screto = random.Random().randrange(1, 100)
    #total_de_tentativa = 0
    pontos = 1000
    print("Qual nível de Dificuldade ?", numero_screto)
    print("(1) é facil (2) Médio (3) Díficil")

    nivel = int(input("Escolha um Nivel : "))
    if nivel == 1:
        total_de_tentativa = 20
    elif nivel == 2:
        total_de_tentativa = 10
    else:
        total_de_tentativa = 5


    for rodada in range(1,total_de_tentativa + 1):
            print("Tentativa {}  de  {}".format(rodada, total_de_tentativa))

            chute = input("Digite o seu numero entre 1 e 100: ")
            chute = int(chute)
            if chute < 1 or chute > 100:
                print("Você deve Digitar um numero entre 1 e 100!")
                continue
            acertou = numero_screto == chute
            Emaior = numero_screto < chute
            manor = numero_screto > chute

            if (acertou):
                print("voce Acertou e fez {} pontos".format(pontos))
                break

            else:
                if Emaior:
                    print("Você erro o seu chute foi maior.")
                elif manor:
                    print("você erro seu chute esta menor")
                pontos_perdidos = abs(numero_screto - chute)# 40 - 20 = 20 pontos
                pontos = pontos - pontos_perdidos

            print("Você erro")

    print("o numero Secreto era ", numero_screto)
    print("fim do jogo")

if __name__ == "__main__":
    jogar()