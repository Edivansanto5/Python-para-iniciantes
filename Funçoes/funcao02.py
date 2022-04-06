def dados(nome, idade=None):
  print('nome: {}'.format(nome))
  if(idade is not None):
    print('idade: {}'.format(idade))
  else:
    print('idade: não informada')

dados('marana')
