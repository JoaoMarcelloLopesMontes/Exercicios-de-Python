def dado():
    ana = 1.10
    mar = 1.50
    n=0
    return ana,mar,n

def compara(ana,mar,n):
    while ana < mar:
        n = n + 1
        ana =  ana + 0.03
        mar = mar + 0.02
    print(f"A ana se tornara maior que a marcia com: ", n, "anos")

def main():
    ana,mar,n = dado()
    print (compara(ana,mar,n))

main()