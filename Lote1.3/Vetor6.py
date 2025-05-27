#Criar e coletar em um vetor [20] com números aleatórios. Classificar este vetor em ordem crescente e mostre os dados

#-Bubble Sort

import random

vet = [random.randint(1,100) for _ in range(20)]

print(f"Vetores fora de ordem: {vet}")

for i in range(0,19,1):
    for j in range(0,20,1):
         if vet[j] > vet[i]:
            vet[i], vet[j] = vet[j], vet[i]


print(f"Valores ordenados: {vet}")
