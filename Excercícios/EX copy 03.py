# Desenvolva um programa que pergunte ao usuário o dia da semana (número de 1 a 7) e exiba o nome do dia correspondente.
dia = (int(input('escolha um numero de 1 a 7:\n ')))
match dia:
    case 1:
        print('Domingo')
    case 2:
        print('Segunda Feira')
    case 3:
        print('Terça Feira')
    case 4:
        print('Quarta Feira')
    case 5:
        print('Quinta Feira')
    case 6:
        print('Sexta Feira')
    case 7:
        print('Sabado')
    case _:
        print('nula')