# Crie um algoritmo que solicite ao usuário uma cor (vermelho, verde, azul) e exiba uma mensagem correspondente à cor escolhida.

cor = (str(input('escolha entre vermelho, azul e verde: \n')))
match cor:
    case 'vermelho':
        print('\033[31m Vermelho\033[m')
    case 'azul':
        print('\033[34m Azul\033[m')
    case 'verde':
        print('\033[32m Verde\033[m')