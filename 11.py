'''
11)Altere o programa anterior, intercalando 3 vetores de 10 elementos cada.
'''
Numeros = [0,1,2,3,4,5,6,7,8,9]
Letras = ['a','b','c','d','e','f','g','h','i','j']
Simbolos = ['A','B','C','D','E','F','G','H','I','J']
lista = ['']*30

for x in range (10):
    lista[x * 3] = Numeros[x]
    lista[x * 3 + 1] = Simbolos[x]
    lista[x* 3 + 2] = Letras[x]

print(lista, end=' ')
