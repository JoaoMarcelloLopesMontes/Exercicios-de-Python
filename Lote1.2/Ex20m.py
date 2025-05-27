def obterdados():
    CoeficienteA = float(input("Digite o coeficiente A: "))
    CoeficienteB = float(input("Digite o coeficiente B: "))
    CoeficienteC = float(input("Digite o coeficiente C: "))
    return CoeficienteA, CoeficienteB, CoeficienteC

def deltacalc(CoeficienteA,CoeficienteB,CoeficienteC):
    Delta = CoeficienteB ** 2 - 4 * CoeficienteA * CoeficienteC
    return Delta
    

    
def main():
    CoeficienteA,CoeficienteB,CoeficienteC = obterdados()
    Resultado = deltacalc(CoeficienteA,CoeficienteB,CoeficienteC)
    if Resultado >= 0:
        X1 = (- CoeficienteB + Resultado ** (1/2)) / (2 * CoeficienteA)
        X2 = (- CoeficienteB - Resultado ** (1/2)) / (2 * CoeficienteA)
        print(X1,X2)
    else:
        print("Não há raízes reais")


if __name__ == "__main__":
    main()