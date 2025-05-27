base = int(input("Digite a base do expoente: "))
expo = int(input("Digite o expoente "))
res = 1 
for i in range(1,expo +1):
  res = res * base
  print(res)