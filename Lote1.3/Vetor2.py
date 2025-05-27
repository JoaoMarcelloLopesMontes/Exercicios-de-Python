#Criar e coletar um vetor [100] inteiro e exibir:

#a. O maior e o menor valor;

#b. A média dos valores.


Vetor = []

for i in range(100):
    coleta = int(input(f"Digite o {i + 1} numero: "))
    Vetor.append(coleta)

print("\nVetor:", Vetor)

maior = Vetor[0]
menor = Vetor[0]
med = 0


for i in Vetor:
    
    if i > maior:
        maior = i
    if i < menor:
        menor = i
    med += i


med = med/100

print(f"maior numero: {maior}")
print(f"menor numero: {menor}")
print(f"Media dos valores do array: {med}")

