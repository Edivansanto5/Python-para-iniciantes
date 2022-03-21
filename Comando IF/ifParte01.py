nota1 = float(input('informe um numero: '))
nota2 = float(input('informe um numero: '))
media = (nota1 + nota2)/2
if(media >= 7):{
    print('parabens vc esta aprovado',media)
}
if(media > 4 & media <6  ):{
    print('vc esta de prova final ',media)
}
if (media <= 4):{
    print('vc esta reprovado ',media)
}