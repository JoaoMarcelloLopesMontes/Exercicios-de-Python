Num = int(input("Digite o numero: "))
fato = 1
fat = 0
for n in range(1, Num + 1):
  fato = fato * n
  fat = fat + (1/fato)
  print(fat)