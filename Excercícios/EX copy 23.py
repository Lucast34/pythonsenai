# Crie um algoritmo que peça ao usuário uma palavra e verifique se a palavra é "Python".
plvr = str(input('digite uma palavra:\n'))

match plvr:
    case 'python':
        print('Acertou a palavra :D')
    case _:
        print('Puts errou :/')
