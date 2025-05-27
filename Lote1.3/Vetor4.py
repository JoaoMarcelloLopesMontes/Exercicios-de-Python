#Criar e coletar em um vetor [30] real e calcular e exibir:

#a. A média do grupo;

#b. A quantidade de notas acima do grupo;

#c. As posições dos valores abaixo da média do grupo.

vet = []
med = 0
somamed = 0
notaacima = 0

for i in range(30):
    n = int(input(f"Digite a nota do {i+1} aluno: "))
    vet.append(n)


for i in vet:
    med += i 

med = med/30

for i in vet:
    if i > med:
        notaacima += 1
    if i < med:
        print(f"Notas abaixo: {i}")

print(f"Quantidade de notas acima da media: {notaacima}")
print(f"Media dos alunos: {med}")