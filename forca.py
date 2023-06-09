import random
def jogar():
    imprime_Mensagem()
    palavra_secreta = carrega_palavra_secreta()
    enforcado = False
    acertou = False
    erros = 0

    letras =  inicializa_letras(palavra_secreta)

    letras_faltando = int(str(letras.count('_')))
    while(not enforcado and not acertou):

       print(letras)
       chute = infomar_chute()

       if (chute in palavra_secreta):
        marca_chute_correto(chute,letras,palavra_secreta,letras_faltando)
        print(letras)
        print('Ainda faltam acertar {} letras'.format(letras_faltando))
       else:
           erros += 1
       erro =  len(letras)
       enforcado = erros == erro
       acertou = letras_faltando == 0
       if acertou:
        imprime_Mensagem_ganhado()
        print("quantidade tentativa erradas {}".format(erros))

        break
       if enforcado:
           imprime_mensagem_perdedo(palavra_secreta)

def imprime_Mensagem():
    print("********************************")
    print("***Bem-vindo ao jogo de Forca***")
    print("********************************")

def imprime_Mensagem_ganhado():
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")


def imprime_mensagem_perdedo(palavra):
    print("Puxa, você foi enforcado!")
    print("A palavra era {}".format(palavra))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")
    print('a Palavra secreta era {}'.format(palavra))


def carrega_palavra_secreta():
    arquivo = open("palavras.txt", "r")

    palavras = []

    for linha in arquivo:
        linha = linha.strip().upper()
        palavras.append(linha)

    palavra_secreta = palavras[random.randrange(0, len(palavras))]
    return  palavra_secreta
    arquivo.close()

def inicializa_letras(palavra):
   return ["_" for letra in palavra]

def marca_chute_correto(chute,letras,palavra_secreta,letras_faltando):
    index = 0
    for letra in palavra_secreta:
        if chute == letra:
            letras[index] = letra
            letras_faltando = letras_faltando - 1
        index += 1

def infomar_chute():
   chute = input("Qual é a letra?")
   chute = chute.strip().upper()
   return  chute



if __name__ == "__main__":
    jogar()

