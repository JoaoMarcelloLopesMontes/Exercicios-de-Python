def calc(qt,soma):
    for i in range(1,65):
        if i == 1:
            soma += 1
        else:
            qt = qt * 2
            soma += qt
    print(qt)

def main():
    qt = 1
    soma = 0
    print (calc(qt,soma))

main()