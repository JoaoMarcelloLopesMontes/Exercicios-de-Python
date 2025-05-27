Nvolta = int(input("Digite o numero de voltar: "))
ExtCirculo = float(input("Digite a extensão em metros: "))
Duracao = int(input("Duração em minutos: "))

dt = Nvolta * ExtCirculo
dt = dt/ 1000
th = Duracao/60
Vm = dt/th
print("A velocidade média é: ", Vm)

