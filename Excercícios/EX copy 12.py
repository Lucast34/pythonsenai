# Escreva um programa que peça ao usuário para escolher um modo de transporte (carro, bicicleta, a pé) e exiba uma mensagem com a velocidade média correspondente.
veiculo = str(input('escolha um meio de transporte:\n'))

match veiculo:
    case 'bicicleta':
        print('A velocidade média e de 15 km/h')
    case 'carro':
        print('A velocidade média e de 40 km/h')
    case 'a pe':
        print('A velocidade média de um ser humano e de 3,6 km/h')