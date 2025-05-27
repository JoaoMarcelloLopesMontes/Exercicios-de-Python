from datetime import date

def ler_data(prompt):
    print(prompt)
    ano = int(input("Ano: "))
    mes = int(input("Mês: "))
    dia = int(input("Dia: "))
    return date(ano, mes, dia)

def calcular_idade(data_nasc, data_atual):
    anos = data_atual.year - data_nasc.year
    meses = data_atual.month - data_nasc.month
    dias = data_atual.day - data_nasc.day

    if dias < 0:
        meses -= 1
        if data_atual.month == 1:
            ultimo_mes = 12
            ano_aux = data_atual.year - 1
        else:
            ultimo_mes = data_atual.month - 1
            ano_aux = data_atual.year

        dias_no_mes_anterior = (date(ano_aux, ultimo_mes + 1, 1) - date(ano_aux, ultimo_mes, 1)).days
        dias += dias_no_mes_anterior

    if meses < 0:
        anos -= 1
        meses += 12

    return anos, meses, dias

def exibir_idade(anos, meses, dias):
    print(f"Idade: {anos} anos, {meses} meses e {dias} dias.")

def main():
    data_nasc = ler_data("Digite sua data de nascimento:")
    data_atual = ler_data("Digite a data atual:")
    anos, meses, dias = calcular_idade(data_nasc, data_atual)
    exibir_idade(anos, meses, dias)


main()
