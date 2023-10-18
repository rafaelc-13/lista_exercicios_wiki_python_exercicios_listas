'''Faça um Programa que leia um vetor de 10 caracteres,
 e diga quantas consoantes foram lidas. Imprima as consoantes.'''
V = [0]*10
vogais = ('a','e','i','o','u')
cont_cons = 0
for x in range(10):
    V[x] = (input("Digite uma letra: "))
    if V[x] not in vogais:
        cont_cons += 1
print("No vetor apresentado existem ",cont_cons," consoantes.")

