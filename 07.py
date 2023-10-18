'''7)Faça um Programa que leia um vetor de 5 números inteiros, mostre a soma, a multiplicação e os números.'''
Numeros=[0]*5
soma = 0
multi = 1

for x in range (5):
    numero = float(input(f'Digite um valor ({x+1}/5): '))
    Numeros[x] = numero
    soma += numero
    multi *= numero
print(f'Se tomarmos esses valores: {Numeros}. \n'
      f'E somarmos, o resultado é: {soma} \n'
      f'E se multiplicarmos, o resultado é: {multi}')
