'''
    O range é um tipo de eqüência imutável de números e	é comumente	usado para looping de um número	específico de vezes	em um comando for já que representam um intervalo.O	comando	range gera um valor	contendo números inteiros sequenciais,	obedecendo a sintaxe: range(inicio,	fim)

'''
print('esplicando o conceito de range e de como ele funciona')

seguencia = range(1,10)
print(seguencia)

for valor in range(1,10):
    print(valor)
print('fim de execusão')