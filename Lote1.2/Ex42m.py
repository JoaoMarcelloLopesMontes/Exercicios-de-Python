def res():
    den = 1
    fato = 0
    for i in range (1,51):
        fato = fato + ( i/den)
        den = den + 2
        print (fato)

def main():
     print (res())

main()