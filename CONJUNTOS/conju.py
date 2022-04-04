'''
Usos básicos incluem testes	 de	 associação	 e	 eliminação	 de	 entradas	 duplicadas.Os objetos	 de conjunto também	 suportam	 operações	 matemáticas como	 união,	 interseção,diferença e	diferença simétrica.Podemos	transformar	um	texto	em	um	conjunto	com	a	frunção	set() e	testar	os	operações:

'''
a = set('abacaxi')
b = set('macaco')

print(a)
print(b)
# fazendo a diferença 
difereca = a-b # - diferença
uniao = a | b # | união das lertras
intersecao = a & b # & interseção das letras das palavras
diferecaSimetrica = a ^ b # ^ diferençaSimetrica

print(difereca)
print(uniao)
print(intersecao)
print(diferecaSimetrica)