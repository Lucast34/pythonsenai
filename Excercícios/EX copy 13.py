# Crie um algoritmo que solicite ao usuário um mês do ano (1 a 12) e exiba a estação do ano correspondente.
mes = int(input('Por favor, informe o mês:\n'))

if (mes > 2 and mes < 7 ):
    print('outono')
elif(mes >= 7 and mes < 10):
    print('inverno')
elif(mes >= 10):
    print('primavera')
else:
    print('verao')





# match mes:
#     case 3,4,5,6:
#         print('outono')
#     case  7,8,9:
#         print('inverno')
#     case 10,11,12:
#         print ('primavera')
#     case 1,2:
#         print ('verão')