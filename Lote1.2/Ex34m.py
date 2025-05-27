def dado():
    Ntab =  int(input("Digite o numero: "))
    return Ntab

def loop(ini,fim):
        return range(ini,fim + 1)

def calc(numero,Ntab):
      return  numero * Ntab

def exib(numeros,Ntab):
      for num in numeros:
            print(calc(num,Ntab))

def main():
      ini = 1
      fim = 10
      Ntab = dado()
      numeros = loop(ini,fim)
      exib(numeros,Ntab)

main()