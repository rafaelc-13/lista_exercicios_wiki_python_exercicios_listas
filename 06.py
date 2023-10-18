'''7)Faça um Programa que peça as quatro notas de 10 alunos,
 calcule e armazene num vetor a média de cada aluno,
  imprima o número de alunos com média maior ou igual a 7.0.'''

Media_Aluno = [0]*10
Nome_Aluno = [0]*10

for x in range (10):
    nome = input(f"Qual o nome {x+1}º do aluno: ")
    Nome_Aluno[x] = nome
    soma = 0
    for y in range (4):
        nota = float(input(f"Digite a {y+1}ª nota do {nome}: "))
        soma += nota
    media = soma/4
    Media_Aluno[x] = media

for z in range (10):
    if Media_Aluno[z] >=7:
        print(f"{Nome_Aluno[z]} passou com média {Media_Aluno[z]}")
    elif Media_Aluno[z] < 7:
        print(f"{Nome_Aluno[z]} não passou pois teve média {Media_Aluno[z]}")




