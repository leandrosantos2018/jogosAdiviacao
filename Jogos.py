import adiviacao
import forca

def Escolher_jogo():
    print("********************************")
    print("********Escolha seu Jogo********")
    print("********************************")

    print("(1) Forca (2) Adivianhação")

    jogo = int(input("Escolher qual Jogo :  "))

    if jogo ==1:
        print("jogando Forca")
        forca.jogar()


    elif jogo == 2:
        print("Jogando Adivianhação")
        adiviacao.jogar()

if(__name__ == "__main__"):
    Escolher_jogo()