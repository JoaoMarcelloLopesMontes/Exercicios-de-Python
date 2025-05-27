def calc():
    res = 0
    sinal = 1

    for i in range(1,16):
        dem = i
        dem = dem * dem
        t = sinal * (i/dem)
        res = res + t
        sinal = -sinal
    print(res)

def main():
    print (calc())

main()