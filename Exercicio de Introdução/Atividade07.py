
repostaCerta = 34
chute = int(input('Digite um numero para ver se vc acerta '))
if(repostaCerta == chute):
    print('*** Acertou mizeravel*** ') 
    print('')
if(chute > repostaCerta):
    print('Seu chute está ACIMA do número correto')
    print('')
if(repostaCerta == chute):
    print('*** Acertou parabéns****')  
while(chute != repostaCerta):
    print('Você errou tente de novo: ')
    chute = int(input('Digite um numero para ver se vc acerta: '))
    print('')
    if(repostaCerta == chute):
        print('Acertou mizeravel ') 
        print('')
    if(chute > repostaCerta):
        print('Seu chute está ACIMA do número correto')
        print('')
    if(chute < repostaCerta):
        print('Seu chute está ABAIXO do número certo ')
        print('')
print('fim de jogo')