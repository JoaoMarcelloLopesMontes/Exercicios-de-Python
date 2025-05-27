#Criar e coletar valores inteiros nos vetores VT1[3] e VT2[3]. 
# Concatenar esses valores em um 3º vetor (VT3[6]) e mostrar os seus dados. P. 
# ex: VT1| 1| 2| 3| |VT2| 4| 5| 6| |VT3| 1| 2| 3| 4| 5| 6

vet1=[]
vet2=[]
vet3=[]

for i in range(3):
    n = int(input(f"Digite o { i + 1} numero: "))
    vet1.append(n)



for i in range(3):
    num = int(input(f"Digite o { i + 1} numero: "))
    vet2.append(num)
vet3 = vet1 + vet2

print(vet1)
print(vet2)
print(vet3)
