pessoa = {'nome':'Marcos ','Idade':23 ,'Cidade':'Picos'}
pessoa['Pais'] = 'Espanha'
pessoa.keys()

print(pessoa.keys())
print(pessoa.values())
print(pessoa)
print(pessoa['nome'])
print(pessoa['Idade'])
print(pessoa['Idade'])
#print(pessoa[0])# vai ocorrer um erro
#print(pessoa.nome) tambem vai ocorrer um erro

a = dict(um=1,dois=2,tres=3,quatro=2+2)#podemos fazer operaçoes dentro de uma criaçao de um dicionario

print(a)