div = list()
contador = None

numero = int(input('Informe o numero: '))

for i in range (1, numero+1):
    if numero % i == 0:
        div.append(i)
        print('os mutiplo são:',div)