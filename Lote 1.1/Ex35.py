
Num1 = int(input("Digite o primeiro número: "))
Num2 = int(input("Digite o segundo número: "))


if Num1 > Num2:
    maior = Num1
    menor = Num2
else:
    maior = Num2
    menor = Num1

soma = 0


for n in range(menor, maior + 1):  
    if n % 2 != 0:  
        soma = soma + n


print( soma)
