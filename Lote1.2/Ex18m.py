def obtendoInf():
  Num1 = int(input("Digite o primeiro numero: "))
  Num2 = int(input("Digite o segundo numero: "))
  return Num1, Num2 

def diferenciando_esses_dois_numeros_funcao(Num1, Num2):
  if Num1 > Num2:
    diferent =  Num1 - Num2
  else:
    diferent =  Num2 - Num1
  return diferent
  
def main():
  Num1,Num2 = obtendoInf()
  diferent = diferenciando_esses_dois_numeros_funcao(Num1, Num2)
  print("A diferença é: ", diferent)
main()


if __name__ == "__main__":
    main()