meses_ano = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho",
             "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]

for indice, mes in enumerate(meses_ano):
    print(f'{indice + 1} -{mes}')

mes_escolhido = int(input('Informe o numero do mês escolhido: '))

if (mes_escolhido > 2 and mes_escolhido < 7):
    print('outono')
elif (mes_escolhido >= 7 and mes_escolhido < 10):
    print('inverno')
elif (mes_escolhido >= 10):
    print('primavera')
else:
    print('verao')
