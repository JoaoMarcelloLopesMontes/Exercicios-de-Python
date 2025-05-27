Num1 = int(input("Digite o primeiro numero: "))
Num2 = int(input("Digite o segundo numero: "))

if Num1 > Num2:
  
  if Num1 % Num2 == 0:
    
    print("O maior é multiplo do menor")
    
  else:
    
    print("O Maior não é multiplo do menor")
    
else:
  if Num2 % Num1 == 0:
    print("O maior  é multiplo do menor")

  else:
    print("O maior não é multiplo do menor")