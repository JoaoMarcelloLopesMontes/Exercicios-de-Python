def dado():
    TI = int(input("Digite o tipo de investimento (1,2): "))
    VI = float(input("Digite o valor investido: "))
    return TI,VI 

def defin(TI,VI):
        
    if (TI > 2) or (TI < 1):
  
        rend = "Nao existe esse valor relacionado á algum investimento"
  
    else: 
  
        if  TI == 1:
    
            rend = VI * 1.03
                
        else:
            rend = VI * 1.05

    return rend

def main():
    TI,VI = dado()
    Renda = defin(TI,VI)
    print(f"Status: ",Renda)

main()
    
                