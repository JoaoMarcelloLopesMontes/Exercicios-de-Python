def dado():
    n1 = int(input("Digite o 1 numero: "))
    n2 = int(input("Digite o 2 numero: "))
    return n1,n2

def  compara(n1,n2):
    if n1 > n2:
        maior = n1
        menor = n2
    else:
        maior = n2
        menor = n1
    return maior,menor

def verifica(maior,menor):
    for i in range(menor, maior + 1):
        if i == 2 or i == 3 or i == 5 or i == 7:
                print(i)
        else:
            if (i % 2 != 0) and (i % 3 != 0) and (i % 5 != 0) and (i % 7 != 0) and ( i != 1):
                print(i)

def main():
    n1,n2 = dado()
    maior,menor = compara(n1,n2)
    print (verifica(maior,menor))

main()