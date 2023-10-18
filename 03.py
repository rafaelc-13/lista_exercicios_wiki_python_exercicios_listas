'''3)Faça um Programa que leia 4 notas, mostre as notas e a média na tela'''
A = [0]*4
soma = 0
for x in range (4):
    A[x] = float(input(f"Qual a {x+1}º nota? "))
    while (A[x] > 10) or (A[x] < 0):
        A[x] = float(input(f"Nota inválida, tente novamente. \n"
                         f"Qual a {x+1}º nota? "))

    soma += A[x]
media = soma/4
print(f"As notas individuais foram :{A}. \n"
      f"A média geral é: {media}")
