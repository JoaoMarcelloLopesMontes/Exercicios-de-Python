def dado():
    HoraIni = int(input("Digite a hora Inicial: "))
    HoraFin = int(input("Digite a hora Final: "))
    MinIni = int(input("Digite o minuto Inicial: "))
    MinFin = int(input("Digite o minuto Final"))
    return HoraFin,HoraIni,MinIni,MinFin

def Temps(HoraFin,HoraIni,MinIni,MinFin):
    if HoraIni > HoraFin:
        Horas = (HoraFin - HoraIni) + 24
    else:
        Horas =  HoraFin - HoraIni


    if MinIni > MinFin:
            Minutos = (MinFin - MinIni) + 60
            Horas = Horas - 1
    else:
            Minutos = MinFin - MinIni

    resultado = "O show durou: ", str(Horas),":", str(Minutos)
    return resultado

def main():
    HoraFin,HoraIni,MinIni,MinFin = dado()
    Result = Temps(HoraFin,HoraIni,MinIni,MinFin)
    print(Result)

main()