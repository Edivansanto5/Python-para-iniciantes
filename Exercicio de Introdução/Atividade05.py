'''
    Com	o conteúdo aprendido até aqui já é possível	começar	a escrever o primeiro script.Crie um arquivo programa.py e faça um	código	que	vai	pedir que o	usuário	entre com	8 notas do tipo float,em seguida,o programa	deve imprimir a media do aluno
    o nome do aluno.
'''
nome = str(input('Informe seu nome: '))
nota1 = float(input('Digite sua nota 1 : '))
nota2 = float(input('Digite sua nota 2 : '))
nota3 = float(input('Digite sua nota 3 : '))
nota4 = float(input('Digite sua nota 4 : '))
nota5 = float(input('Digite sua nota 5 : '))
nota6 = float(input('Digite sua nota 6 : '))
nota7 = float(input('Digite sua nota 7 : '))
nota8 = float(input('Digite sua nota 8 : '))
somaMedia = (nota1 + nota2 + nota3 + nota4 + nota5 + nota6 + nota7 + nota8)/8
print('Olá ', nome , ' Sua Média é ',somaMedia)

