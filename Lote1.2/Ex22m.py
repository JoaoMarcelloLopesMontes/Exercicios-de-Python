def dados():
    n1 = int(input("Digite o valor do primeiro numero: "))
    n2 = int(input("Digite o segundo numero: "))
    return n1,n2

def compara(n1,n2):
    if n1 < n2:
        resultado = "O maior é o: " + str(n2) + " e o menor é: " + str(n1) + " Portanto sua ordem crescente é: " + str(n1) + "," + str(n2)
    else:
        resultado = "O maior é o: " + str(n1)+ " e o menor é: " + str(n2) + " Portanto sua ordem crescente é: " + str(n2) + "," + str(n1)
    return resultado

def main():
    n1,n2 = dados()
    Exib = compara(n1,n2)
    print(Exib)


main()
