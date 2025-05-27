from datetime import date

ano_nasc = int(input("Ano de nascimento: "))
mes_nasc = int(input("Mês de nascimento: "))
dia_nasc = int(input("Dia de nascimento: "))

ano_atual = int(input("Ano atual: "))
mes_atual = int(input("Mês atual: "))
dia_atual = int(input("Dia atual: "))


data_nasc = date(ano_nasc, mes_nasc, dia_nasc)
data_atual = date(ano_atual, mes_atual, dia_atual)


anos = ano_atual - ano_nasc
meses = mes_atual - mes_nasc
dias = dia_atual - dia_nasc


if dias < 0:
    meses -= 1
    if mes_atual == 1:
        ultimo_mes = 12
        ano_aux = ano_atual - 1
    else:
        ultimo_mes = mes_atual - 1
        ano_aux = ano_atual

    dias_no_mes_anterior = (date(ano_aux, ultimo_mes + 1, 1) - date(ano_aux, ultimo_mes, 1)).days
    dias += dias_no_mes_anterior

if meses < 0:
    anos -= 1
    meses += 12


print(f"Idade: {anos} anos, {meses} meses e {dias} dias.")
