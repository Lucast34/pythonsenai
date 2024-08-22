#Crie um algoritmo que pergunte ao usuário um número e verifique se ele é múltiplo de 3.
numero = int(input('Digite um numero:\n'))

if numero % 3 == 0:
    print('Esse numero é múltiplo de 3')
else:
    print('Esse numero não é múltiplo de 3')