'''8)Faça um Programa que peça a idade e a altura de 5 pessoas, armazene cada informação no seu respectivo vetor. Imprima a idade e a altura na ordem inversa a ordem lida.'''
Nomes = [0]*5
Idades = [0]*5
Alturas = [0]*5

for x in range (5):
    nome = input("Qual seu nome? ")
    Nomes[x] = nome
    idade = int(input(f"{Nomes[x]}, qual a sua idade? "))
    Idades[x] = idade
    altura = float(input(f"{Nomes[x]}, qual a sua altura? "))
    Alturas[x] = altura

print(f"Obrigado pelas informações!")
for y in range (4,-1,-1):
    print(f"{y+1}º nome: {Nomes[y]}, com {Idades[y]} anos de idade e {Alturas[y]} metros de altura.")

