def dado():
    Num1 = int(input("Digite o primeiro número: "))
    Num2 = int(input("Digite o segundo número: "))
    return Num1,Num2

def verfMaior(Num1,Num2):
    if Num1 > Num2:
        maior = Num1
        menor = Num2
    else:
        maior = Num2
        menor = Num1
    return maior,menor

def somas(maior,menor,soma):
    for  n in range(menor,maior + 1):
        if n % 2 != 0:
            soma += n 
    
    return soma

def main():
    soma = 0
    Num1,Num2 = dado()
    maior,menor = verfMaior(Num1,Num2)
    print (somas(maior,menor,soma))
    
main()
