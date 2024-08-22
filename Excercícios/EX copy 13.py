# Crie um algoritmo que solicite ao usuário um mês do ano (1 a 12) e exiba a estação do ano correspondente.
mes = int(input('Por favor, informe o mês:\n'))

match mes:
    case 3,4,5,6:
        print('outono')
    case  7,8,9:
        print('inverno')
    case 10,11,12:
        pirnt ('primavera')
    case 1,2:
        print ('verão')