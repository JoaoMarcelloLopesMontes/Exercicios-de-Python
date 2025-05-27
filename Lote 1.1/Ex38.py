num = int(input("Digite o número: "))  
maior = num
menor = num

for n in range(1, 100):  
    num = int(input("Digite o número: "))

    if num > maior:
        maior = num  
    elif num < menor:
        menor = num  

print("Maior número: ", maior)
print("Menor número: ", menor)
