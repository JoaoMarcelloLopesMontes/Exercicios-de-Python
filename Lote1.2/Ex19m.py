def obtendo():
  Num1 = int(input("Digite o primeiro numero: "))
  Num2 = int(input("Digite o segundo numero: "))
  return Num1, Num2

def Maaior(Num1,Num2):
  if Num1 >= Num2:
    Maior = Num1
  else:
    Maior = Num2
  return Maior

def main():
  Num1, Num2 = obtendo()
  Solucao = Maaior(Num1,Num2)
  print("O maior numeor digitado é: ", Solucao)


if __name__ == "__main__":
    main()