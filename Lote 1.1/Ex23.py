n1 = int(input("Digite o 1 número: "))
n2 = int(input("Digite o 2 número: "))
n3 = int(input("Digite o 3 número: "))
n4 = int(input("Digite o 4 número: "))

if n4 > n3:
  print("Ordem crescente: ", n1,n2,n3,n4)
else:
  if  n4 > n2:
    print("Ordem crescente: ", n1,n2,n4,n3)
  else:
    if n4 > n1:
      print("Ordem crescente: ", n1,n4,n2,n3)
    else:
      print("Ordem crescente: ", n4,n1,n2,n3)
