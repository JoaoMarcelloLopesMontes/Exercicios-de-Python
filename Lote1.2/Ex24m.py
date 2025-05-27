def dado():
    Valor = int(input("Digite o numero: "))
    return Valor


def  div(Valor):
    if Valor % 2 == 0 and Valor % 3 == 0:
        div = "O valor colocado é divisivel por 2 E por 3"
    else:
        if Valor % 2 == 0:
            div = "O valor é divisivel por 2"
        else:
            if Valor % 3 == 0:
              div = "O valor é divisivel por 3"
            else:
                div = "O valor não é divisivel por 2 nem por 3"
    return div


def main():
    Valor = dado()
    exib = div(Valor)
    print(exib)

main()