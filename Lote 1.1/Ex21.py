Nota1 = float(input("Digite a primeira nota: "))
Nota2 = float(input("Digite a segunda nota: "))
Nota3 = float(input("Digite a terceira nota: "))

Media = (Nota1 + Nota2 + Nota3) / 3

if Media < 3:
    print("Reprovado")
else:
     if Media  >= 3 and Media < 6:
        print("Exame")
     else:
        print("Aprovado")


  
  