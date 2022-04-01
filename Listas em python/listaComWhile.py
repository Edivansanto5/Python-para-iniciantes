meses = ['Janeiro','Fevereiro','Março','Abril','Maio','Junho','Julho','Agosto','Setembro','Outubro','Novembro','Dezembro']

numero = 1

while (numero < 4):
    mes = input('Digite um mês ( 1 - 12): ')
    if 1 <= mes <= 12:
        print('O mes é {}'.format(mes[mes - 1 ]))
    numero += 1