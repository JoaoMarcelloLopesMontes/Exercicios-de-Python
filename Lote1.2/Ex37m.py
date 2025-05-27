def inpt():
    N = int(input("Digite o numero: "))
    return N

def calc(N):
    fin = -1
    febo = 1
    for N in range(1, N + 1):
        res = fin + febo
        fin = febo
        febo = res
        print(res)

def main():
    N = inpt()
    print (calc(N))

main()