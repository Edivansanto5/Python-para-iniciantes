
print('******************************')
print(' * Jogo da adivinhação *')
print('******************************')

repostaCerta = 10
chute = int(input('Digite um numero para ver se você acerta! '))
if(chute == repostaCerta):
    print('Acertou Miseravel !!!! ^ _ ^')
    print('Parabens !!!!')  
if(chute > repostaCerta):
    print('Seu chute está acima da reposta ^ _ ^')
if(chute < repostaCerta):   
    print('Seu chute esta abaixo da reposta ^ _ ^')
print('Fim de jogo !!!')