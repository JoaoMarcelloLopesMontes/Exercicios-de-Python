# Exercício baseado apartir do exercício 6 de vetores 
#- Busca binaria apartir de um vetor ordenado em ordem crescente
#------------------

import random

vet = [random.randint(1,50) for _ in range(20)]

print(f"Vetor desordenado: {vet}")

for i in range(0,19,1):
    for j in range(i + 1,20,1):                                                                                                               
         if vet[i] > vet[j]:
            vet[j], vet[i] = vet[i], vet[j]
print(f"Vetor ordenado: {vet}")

#Pesquisa binaria

numBusca = int(input(f"Digite o numero que deseja buscar: "))

inicio = 0
fim =  19
meio = 0

while inicio <= fim:
    med = (fim + inicio) / 2
    cod = int(med)

    if vet[cod] == numBusca:
        print(f"Numero existe e esta localizado no index: {cod}")
        break
    elif vet[cod] < numBusca:
         inicio += 1
    else:
        fim -= 1

if inicio > fim:
    print("Nao existe")
