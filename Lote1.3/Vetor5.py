#Criar e coletar em um vetor [20] inteiro. Calcule e exiba, segundo:

vet = []
cont = 19
contando = 0
soma = 0

for i in range(20):
    n = int(input(f"Digite o {i + 1} numero: "))
    vet.append(n)


for i in range(10):
     resultado = vet[i] - vet[19 - i]
     soma += resultado

print(soma)