def loop(ini,fim):
    return range(ini,fim + 1)

def quad(numero):
    return numero * numero

def exib_quad(numeros):
    for num in numeros:
        print(quad(num))


def main():
    ini = 10
    fim = 150
    numeros = loop(ini, fim)
    exib_quad(numeros)   

main()      
