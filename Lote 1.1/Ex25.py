HoraIni = int(input("Digite a hora Inicial: "))
HoraFin = int(input("Digite a hora Final: "))
MinIni = int(input("Digite o minuto Inicial: "))
MinFin = int(input("Digite o minuto Final"))



if HoraIni > HoraFin:
  Horas = (HoraFin - HoraIni) + 24
else:
  Horas =  HoraFin - HoraIni



if MinIni > MinFin:
  Minutos = (MinFin - MinIni) + 60
  Horas = Horas - 1
else:
  Minutos = MinFin - MinIni


print("O show durou: ", Horas,":", Minutos)


