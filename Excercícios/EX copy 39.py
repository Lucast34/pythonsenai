# Crie um algoritmo que peça ao usuário para digitar uma senha e verifique se a senha é "1234".
s1 = int(input('Digite uma senha (numero apenas.):\n'))

match s1:
    case 1234:
        print('sua senha é muito fraca')
    case _:
        print('sua senha é forte')

