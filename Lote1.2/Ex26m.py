def dados():
    Num1 = int(input("Digite o primeiro numero: "))
    Num2 = int(input("Digite o segundo numero: "))
    return Num1,Num2

def compara(Num1,Num2):
    if Num1 > Num2:
  
        if Num1 % Num2 == 0:
            Res = "O maior é multiplo do menor"
    
        else:
    
            Res = "O Maior não é multiplo do menor"
    
    else:
        if Num2 % Num1 == 0:
             Res = "O maior  é multiplo do menor"

        else:
            Res = "O maior não é multiplo do menor"
    return Res

def main():
    Num1,Num2 = dados()
    Exib = compara(Num1,Num2)
    print(Exib)


main()