def dado():
    Num = int(input("Digite o numero para ser fatoriado: "))
    return Num

def calc(Num,Res):
    for Num in range (1,Num + 1):
        Res = Res * Num
    return Res

def  main():
    Res = 1
    Num = dado()
    print (calc(Num,Res))

main()