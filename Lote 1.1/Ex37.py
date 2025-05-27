Fin = -1
Febo = 1
N = int(input("Digite o numero: "))

for n in range(1, N +1):
  res = Fin + Febo
  Fin = Febo
  Febo = res
  print(res)