def dado():
    PrecoAtual = float(input("Digite o valor atual: "))
    MediaMes =  int(input("Digite a media mensal: "))
    return PrecoAtual,MediaMes

def calc(PrecoAtual,MediaMes):
    if  MediaMes < 500  and PrecoAtual < 30:
        Novopreco =  PrecoAtual * 1.10
    else:
        if (MediaMes >= 500 and MediaMes < 1000) and (PrecoAtual >= 30 and PrecoAtual < 80):
            Novopreco = PrecoAtual * 1.15
        else:
            if MediaMes >= 1000 and PrecoAtual >= 80:
                Novopreco = PrecoAtual * 0.95
            else:
                Novopreco = PrecoAtual
    return Novopreco

def main():
    PrecoAtual,MediaMes = dado()
    Ajuste = calc(PrecoAtual,MediaMes)
    print(f"O ajuste ficou: ", Ajuste)


main()
