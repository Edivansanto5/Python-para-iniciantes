from operator import index

print('******************************************************')
print('**********Jogo da forga 2.0 ********************')
print('******************************************************')
palavra_secreta = 'banana'
letras_acertadas = ['_','_','_','_','_','_']
enforcou = False
acertou = False
erros = 0
print(letras_acertadas)
while(not enforcou and not acertou):
    chute = input('Digite uma letra ')
    if(chute in palavra_secreta):
        posicao = 1
        for letra in palavra_secreta:
            if(chute.upper() == letra.upper()):
                letras_acertadas[letras_acertadas] = letra
            posicao = index + 1
    else:
        erros += 1
        enforcou = erros == 6
        acertou = '_' not in letras_acertadas
        print(letras_acertadas)
    if(acertou):
        print('Você Ganhou !!!')
    else:
        print('Você Perdeu !!!!!')
print('Fim de jogo')
           
