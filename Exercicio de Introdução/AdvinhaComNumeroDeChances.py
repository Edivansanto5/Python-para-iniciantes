'''
    Vamos atualizar o nosso jogo e da um numero de chance para o nosso jogador!
'''
numeroSecreto = 15
totalDeTentivas = 5
while(totalDeTentivas > 0): 
    palpite = int(input('Digite um numero para saber se vc sabe o numero Secreto: '))
    print('Voce Digitou ',palpite)
    
    #comparação entre os valores
    acertou = palpite == numeroSecreto
    maior = palpite > numeroSecreto
    menor = palpite < numeroSecreto
    
    if(acertou):
        print('Acertou mizeravel ')
        break
    elif(maior):
        print('Seu chute está ACIMA do numero segreto ')
    elif(menor):
        print('Seu chute está ABAIXO do numero segreto ')
    totalDeTentivas = totalDeTentivas - 1
print('Fim de jogo')
    