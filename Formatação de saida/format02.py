nota1 = float(input('Digite uma nota: '))
nota2 = float(input('digite outro nota '))
nome  = str(input('Informe seu nome: '))
sexo = str (input('Informe seu sexo: '))

#vamos calcular a media dessa pessoa e exibir a media, e saber seu nome e sexo;
somaNota = nota1 + nota2
mediaNotas = somaNota/2

print('Olá {} Sua média é {:.2f} e você e do sexo {}'.format(nome.capitalize(),mediaNotas,sexo))

# nome.capitalize() vai mostrar a primeira letra do nome maiscula
#{:.2f} vai formatar a variavel mediaNotas e duas casas decimal após a virgula