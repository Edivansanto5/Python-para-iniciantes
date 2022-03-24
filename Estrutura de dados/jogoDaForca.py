print("************************************")
print('*****Bem vindo ao Jogo da Forca*****')
print('************************************')
palavraSecreta = 'banana'
acertou = False
enforcou = False
while(not acertou and not enforcou):
    chute = input('Digite uma letra')
    posicao = 0
    for letra in palavraSecreta:
        if(chute == letra):
            print('Achei a letra {} na posisao {}'.format(letra,index))
        posicao = posicao - 1
        print('continua')
    
