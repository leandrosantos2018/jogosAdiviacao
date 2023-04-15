import random


print("********************************")
print("Bem-vindo ao jogo de Adivinhação")
print("********************************")

#gerando numero aleatori com biblioteca Random
numero_screto = random.Random().randrange(1,100)

total_de_tentativa = 3


for  rodada in range(1,total_de_tentativa + 1):
        print("Tentativa {}  de  {}".format(rodada,total_de_tentativa))
        chute = input("Digite o seu numero entre 1 e 100: ")
        chute = int(chute)
        if(chute <1 or chute > 100):
            print("Você deve Digitar um numero entre 1 e 100!")
            continue
        acertou = numero_screto == chute
        Emaior  =  numero_screto < chute
        manor   =  numero_screto > chute

        if (acertou):
            print("voce Acertou")
            break

        else:
            if Emaior:
                print("Você erro o seu chute foi maior.")
            elif (manor):
                 print("você erro seu chute esat menor")

        print("Você erro")



print("o numero Secreto era " , numero_screto)
print("fim do jogo")


