'''
    Dada a lista = [12,-2,4,8,29,45,78,36,-17,2,12,8,3,3,-52]faça um programa que:
    a)imprimao maior elemento
    b)imprimao menor elemento
    c)imprimaos	números	pares
    d)imprimao número de ocorrências do	primeiro elemento da lista
    e)imprimaa média dos elementos
    f)imprimaa soma	dos	elementos de valor negativo
'''
# a)imprimao maior elemento
lista = [12,-2,4,8,29,45,78,36,-17,2,12,8,3,3,-52];
valorMaximo = max(lista)# função max() com o parametro o node da lista
print('Valor Máximo',valorMaximo)

#b)imprimao menor elemento
lista = [12,-2,4,8,29,45,78,36,-17,2,12,8,3,3,-52]
valorMinino = min(lista)
print('Valor Minimo',valorMinino)
print('Números Pares')

#c)imprima os números pares
for pares in lista:
    if pares % 2 == 0:
        print(pares)
print(' ')

print('Números Impares')
# imprima os numeros impares
for impar in (lista):
    if impar % 2 == 1:
        print(impar)
print('espaços')
print('teste')

