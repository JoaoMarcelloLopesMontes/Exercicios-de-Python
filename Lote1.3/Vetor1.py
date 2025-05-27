#Criar e coletar um vetor [50] inteiro. Calcular e exibir:

#a. A média dos valores entre 10 e 200;

#b. A soma dos números ímpares


vetor = []

for i in range(50):
    numero = int(input(f"Digite o {i + 1}º número: "))
    vetor.append(numero)

print("\nVetor:", vetor)

medvet10_200 = 0
somaimp = 0
contador = 0

for i in vetor:
    if  10 <= i >=200:
        medvet10_200 += i
        contador  += 1
    if i % 2 != 0:
        somaimp += i 

medvet10_200 = medvet10_200 /contador

print(f"\n A media dos valores é: {medvet10_200}")
print(f"\n A soma dos valores impares é: {somaimp}")