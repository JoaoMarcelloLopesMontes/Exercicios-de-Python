Valor = int(input("Digite o numero: "))

if Valor % 2 == 0 and Valor % 3 == 0:
  print("O valor colocado é divisivel por 2 E por 3")
else:
  if Valor % 2 == 0:
    print("O valor é divisivel por 2")
  else:
    if Valor % 3 == 0:
      print("O valor é divisivel por 3")
    else:
      print("O valor não é divisivel por 2 nem por 3")