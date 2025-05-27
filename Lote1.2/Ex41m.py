def dado():
    for i in range(1,7):
        for ia in range (1,7):
            if  i + ia == 7:
                print(i, "+", ia, "= 7")

def main():
    print (dado())

main()