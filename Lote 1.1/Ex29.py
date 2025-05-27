TI = int(input("Digite o tipo de investimento (1,2): "))
VI = float(input("Digite o valor investido: "))

if (TI > 2) or (TI < 1):
  
  print("Nao existe esse valor relacionado á algum investimento")
  
else: 
  
  if  TI == 1:
    
    rend = VI * 1.03
    print("A renda foi de: ", rend)

  else:
    rend = VI * 1.05
    print("A renda foi de: ", rend)
    
    