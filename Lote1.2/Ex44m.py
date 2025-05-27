def dado():
    base = int(input("Digite a base do expoente: "))
    expo = int(input("Digite o expoente "))
    res = 1
    return base,expo,res

def calc(base,expo,res):
    for i in range(1,expo +1):
        res = res * base
    print(res)
def main():
    base,expo,res = dado()
    print (calc(base,expo,res))
main()