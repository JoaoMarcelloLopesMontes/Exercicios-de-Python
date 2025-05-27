Qt = 1
soma = 0
for i in range(1, 65):
  if i == 1:
    soma = soma + 1
  else:
   Qt = Qt * 2
   soma = soma + Qt
   print(soma)