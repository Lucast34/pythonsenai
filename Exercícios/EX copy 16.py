# Desenvolva um programa que peça ao usuário um tipo de combustível (gasolina, etanol, diesel) e exiba o preço correspondente por litro.
combu = str(input('Qual o combustível que você deseja abastecer:\n'))

match combu:
    case 'gasolina':
        print('6 R$ o litro')
    case 'etanol':
        print('8 R$ o litro')
    case 'diesel':
        print('5 R$ o litro')
    case _:
        print('digite novamente')