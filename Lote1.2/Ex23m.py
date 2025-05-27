def dados():
    n1 = int(input("Digite o 1 número: "))
    n2 = int(input("Digite o 2 número: "))
    n3 = int(input("Digite o 3 número: "))
    n4 = int(input("Digite o 4 número: "))
    return n1,n2,n3,n4

def ordena(n1,n2,n3,n4):
    if n4 > n3:
        ordem = "Ordem crescente: " + str(n1),str(n2),str(n3),str(n4)
    else:
        if  n4 > n2:
         ordem =  "Ordem crescente: " + str(n1),str(n2),str(n4),str(n3)
        else:
            if n4 > n1:
                ordem =  "Ordem crescente: " + str(n1),str(n4),str(n2),str(n3)
            else:
                 ordem = "Ordem crescente: "+ str(n4),str(n1),str(n2),str(n3)
    return ordem


def main():
    n1,n2,n3,n4 = dados()
    exibe = ordena(n1,n2,n3,n4)
    print(exibe)


main()
    
