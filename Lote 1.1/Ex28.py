PrecoAtual = float(input("Digite o valor atual: "))
MediaMes =  int(input("Digite a media mensal: "))


if  MediaMes < 500  and PrecoAtual < 30:
  Novopreco =  PrecoAtual * 1.10
else:
  if (MediaMes >= 500 and MediaMes < 1000) and (PrecoAtual >= 30 and PrecoAtual < 80):
    Novopreco = PrecoAtual * 1.15
  else:
    if MediaMes >= 1000 and PrecoAtual >= 80:
      Novopreco = PrecoAtual * 0.95
    else:
      Novopreco = PrecoAtual

print("O novo preco é: ", Novopreco)