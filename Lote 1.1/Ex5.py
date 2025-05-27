CoeficienteA = float(input("Digite o coeficiente A: "))
CoeficienteB = float(input("Digite o coeficiente B: "))
CoeficienteC = float(input("Digite o coeficiente C: "))

Delta = CoeficienteB ** 2 - 4 * CoeficienteA * CoeficienteC

X1 = (- CoeficienteB + Delta ** (1/2)) / (2 * CoeficienteA)
X2 = (- CoeficienteB - Delta ** (1/2)) / (2 * CoeficienteA)

print(X1,X2)
                                          