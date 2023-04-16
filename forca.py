
def jogar():
    print("********************************")
    print("***Bem-vindo ao jogo de Forca***")
    print("********************************")
                    #b0,a1,n2,a3,n4,a5
    palavra_secreta = "banana".upper()
    enforcado = False
    acertou = False
    letras = ["_", "_", "_", "_", "_", "_"]
    letras_faltando = int(str(letras.count('_')))

    erros = 0


    #enquanto True and True
    while(not enforcado and not acertou):

       chute = input("Qual é a letra?")
       chute = chute.strip().upper()

       if (chute in palavra_secreta):
           index = 0
           for letra in palavra_secreta:
                if chute == letra:
                    letras[index] = letra
                    letras_faltando = letras_faltando - 1
                index += 1
           print(letras)
           print('Ainda faltam acertar {} letras'.format(letras_faltando))
       else:
           erros += 1

       enforcado = erros == 6
       acertou = letras_faltando ==0
       if acertou:
            print("Você ganhou !!")
            print("quantidade tentativa erradas {}".format(erros))
            break
       if enforcado:
            print("Você perdeu!! a palavra era : {}".format(palavra_secreta))

    print("fim de jogo")

if __name__ == "__main__":
    jogar()



