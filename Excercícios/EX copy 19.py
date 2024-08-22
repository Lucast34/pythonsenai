#Escreva um algoritmo que peça ao usuário o nome de uma fruta e verifique se a fruta é uma maçã.
fruta = (str(input('Digite uma fruta:\n')))

match fruta:
    case 'maçã':
        print('Essa fruta é uma maçã')
    case _:
        print('Essa fruta não é uma maçã')