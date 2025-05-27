#Obtendo os dados...
def obter_dados():
  HorasT = float(input("Digite a quantidade de horas trabalhadas: "))
  ValorH= float(input("Digite o valor da hora trabalhada: "))
  Pdesc = float(input("Digite o percentual de desconto: "))
  NumeroDep = float(input("Digite o número de dependentes: "))
  
  return HorasT,ValorH,Pdesc, NumeroDep

#Calc Salario Bruto
def calc_salB(HorasT,ValorH):
  salBruto = HorasT * ValorH
  
  return salBruto


#Calc Salario Liquido

def calc_saL(NumeroDep,Pdesc,salBruto):
  salLiquido =  salBruto - salBruto * (Pdesc/100)
  salLiquido = salLiquido + (NumeroDep * 100)

  return salLiquido

#Principal 

def main():
  HorasT, ValorH, Pdesc, NumeroDep = obter_dados()
  salBruto = calc_salB(HorasT, ValorH) 
  salLiquido = calc_saL(NumeroDep, Pdesc, salBruto)  
  
  print("Salário líquido é: R$", salLiquido)
  
main()
  
  
  
  
 