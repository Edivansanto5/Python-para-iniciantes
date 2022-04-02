meses = ['Janeiro','Fevereiro','Março','Abril','Maio','Junho','Julho','Agosto','Setembro','Outubro','Novembro','Dezembro']

n= 1

while (n < 4):
    mes = input('Digite um mês ( 1 - 12): ')
    if n <= mes <= 12:
        print('O mes é {}'.format(mes[mes - 1 ]))
    n += 1