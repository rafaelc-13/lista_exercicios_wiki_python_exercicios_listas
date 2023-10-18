'''10)Faça um Programa que leia dois vetores com 10 elementos cada.
 Gere um terceiro vetor de 20 elementos, cujos valores deverão ser
 compostos pelos elementos intercalados dos dois outros vetores.'''

A= [10,9,8,7,6,5,4,3,2,1]
Letras = ['a','b','c','d','e','f','g','h','i','j']
C = [0]*20

for x in range (10):
    C[x * 2] = A[x]
    C[x * 2 + 1] = Letras [x]
print(C,end=' ')
