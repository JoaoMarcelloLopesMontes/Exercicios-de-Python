def dados():
    Nvolta = int(input("Digite o numero de voltar: "))
    ExtCirculo = float(input("Digite a extensão em metros: "))
    Duracao = int(input("Duração em minutos: "))
    return Nvolta,ExtCirculo,Duracao

def calc(Nvolta,ExtCirculo,Duracao):
    dt = Nvolta * ExtCirculo
    dt = dt/ 1000
    th = Duracao/60
    Vm = dt/th
    return Vm

def main():
    Nvolta,ExtCirculo,Duracao = dados()
    Vm = calc(Nvolta,ExtCirculo,Duracao)
    print (f"A velocidade média é: ", Vm)


main()