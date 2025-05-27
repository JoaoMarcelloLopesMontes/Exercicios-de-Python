
def obter_dado():
  tempoP = float(input("Digite o tempo do percurso: "))
  VelocidadeM = float(input("Digite a velocidade media: "))

  return tempoP, VelocidadeM
  
def cal(tempoP, VelocidadeM):
  LitroG =  tempoP * VelocidadeM / 12
  return LitroG
  
def  main():
   tempoP, VelocidadeM = obter_dado()
   LitroG = cal(tempoP, VelocidadeM)
   print("Os litros gastos: ", LitroG)

main()