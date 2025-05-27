HorasTrab = float(input("Digite o número de horas trabalhadas: "))
ValorHora = float(input("Digite o valor da hora trabalhada: "))
PercentualDesc = float(input("Digite o percentual de desconto: "))
NumeroDependentes = float(input("Digite o número de dependentes: "))
SalarioBruto = HorasTrab * ValorHora
SalarioLiq = SalarioBruto - SalarioBruto * (PercentualDesc / 100)
SalarioLiq = SalarioLiq + NumeroDependentes * 100 
print("O salário líquido é: ", SalarioLiq)