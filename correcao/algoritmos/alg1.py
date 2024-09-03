from re import I


numeros_ex = ['um', 'dois', 'três']

numeros = int(input('informe um numero de 1 a 3: '))


if numeros > 3 or numeros < 1:
    print('Erro')

else:
    print(f'seu numero por extenso é:{numeros_ex[numeros-1]}')
