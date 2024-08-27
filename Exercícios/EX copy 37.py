# Desenvolva um algoritmo que peça ao usuário para digitar um número e verifique se ele é múltiplo de 2 ou de 5.
numero = int(input('Digite um numero:\n'))

if numero % 5 == 0 and numero % 2 == 0:
    print('Esse numero é múltiplo por 5 e 2')
else:
    print('Esse numero não é múltiplo por 5 ou 2')