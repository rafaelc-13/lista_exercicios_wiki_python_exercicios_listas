'''
12)Foram anotadas as idades e alturas de 30 alunos. Faça um Programa que determine quantos alunos com mais de 13 anos possuem altura inferior à média de altura desses alunos.
'''
idade=[0]*30
altura=[0]*30
soma_altura = 0

for x in range (30):
    idade[x] = int(input(f"Idade do {x+1}º aluno: "))
    altura[x] = float(input(f"Altura do {x+1}º aluno: "))
    soma_altura += altura[x]
media = soma_altura/30
cont = 0
for y in range (30):
    if idade[y] > 13 and altura[y] < media:
        cont += 1
print(f'A quantidade de alunos maiores de 13 anos com altura menor que a média final {media}, é {cont}.')
