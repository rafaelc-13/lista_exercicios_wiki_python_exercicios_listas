'''9)Faça um Programa que leia um vetor A com 10 números inteiros, calcule e mostre a soma dos quadrados dos elementos do vetor.'''
Vetor = [10,9,8,7,6,5,4,3,2,1]
Quadrado_V = [0]*10
soma = 0

for y in range (10):
    Quadrado_V[y] = Vetor[y] ** 2
    soma += Quadrado_V[y]

print("Se somarmos os quadrados de: ")
for z in range (10):
    print(f"({Vetor[z]} = {Quadrado_V[z]}) ", end = " ")
print(f"\nÉ igual a {soma}")
