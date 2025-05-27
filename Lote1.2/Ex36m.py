def dado():
    Num = int(input("Digite o numero: "))
    return Num


def calc(fato,fat,Num):
    for n in range(1, Num + 1):
            fato = fato * n
            fat = fat + (1/fato)
    print(fat)

def main():
     fato = 1
     fat = 0
     Num = dado()
     print (calc(fato,fat,Num))


main()

                        