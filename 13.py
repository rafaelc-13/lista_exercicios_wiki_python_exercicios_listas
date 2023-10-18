'''
13)Faça um programa que receba a temperatura média de cada mês do ano e armazene-as em uma lista.
Após isto, calcule a média anual das temperaturas e mostre todas as temperaturas acima da média anual,
e em que mês elas ocorreram (mostrar o mês por extenso: 1 – Janeiro, 2 – Fevereiro, . . . ).
'''
meses = ['Janeiro','Fevereiro','Março','Abril','Maio','Junho','Julho','Agosto','Setembro','Outubro','Novembro','Dezembro']
medias_temp = [0]*12
soma = 0

for x in range(12):
    medias_temp[x] = int(input(f"Temperatura média de {meses[x]} foi: "))
    soma += medias_temp[x]
media_das_medias = soma / 12

print(f"Temperaturas acima da média anual ({media_das_medias:.2f}):")
for y in range (12):
    if medias_temp[y] > media_das_medias:
        print(f"{meses[y]}: {medias_temp[y]:.2f}°C")

