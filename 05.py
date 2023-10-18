'''5)Faça um Programa que leia 20 números inteiros e armazene-os num vetor.
 Armazene os números pares no vetor PAR e os números IMPARES no vetor impar.
  Imprima os três vetores.'''
V = [0]*20
V_par = [0]*20
V_impar = [0]*20

for x in range (20):
    valor = int(input("Digite um valor: "))
    V[x] = valor
    if V[x] % 2 == 0:
        V_par[x] = V[x]
    elif V[x] % 2 != 0:
        V_impar[x] = V[x]

print(f"Os valores foram: {V} ")
print(f"Os valores pares foram: ")
for y in range (20):
    if V_par[y] != 0:
        print(V_par[y],end = " ")

print(f"\nOs valores impares foramforam:")
for z in range (20):
    if V_impar[z] != 0:
        print(V_impar[z],end = " ")
