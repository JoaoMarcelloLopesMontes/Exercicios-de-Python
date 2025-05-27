def dado():
    num = int(input("Digite o número: "))  
    maior = num
    menor = num
    return maior,menor

def prox(maior,menor):
    for n in range(1,5):
        num = int(input("Digite o número: "))
        if num > maior:
            maior = num  
        elif num < menor:
            menor = num  

    print("Maior número: ", maior)
    print("Menor número: ", menor)

def main():
    maior,menor = dado()
    print (prox(maior,menor))

main()       

