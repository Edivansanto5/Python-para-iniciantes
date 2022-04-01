mes	=	['Janeiro',	'Fevereiro',	'Março',	'Abril',	'Junho',	'Julho',	'Agosto',	'Setembro',	'Outubro','Novembro',	'Dezembro']

n=1
while(n<12):
	mes	=	input("Escolha um mês	(1-12):	")
	if (1 <= mes <= 12):
		print('O mês é {}'.format(mes[mes-1]))
	n+=1