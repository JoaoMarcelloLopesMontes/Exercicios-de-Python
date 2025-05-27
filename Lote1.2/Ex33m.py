def dado():
    Num = int(input("Digite o numero: "))
    return Num

def calc(Num,Res):

    for n in range(Num):
        n =  n + 1
        print(1,"/",n)
        Res = Res + (1/n)
        print(Res)

def main():
    Num = dado()
    Res = 0
    print (calc(Num,Res))

main()