# Escreva um algoritmo que peça ao usuário para digitar um número e verifique se ele é maior, menor ou igual a 10.
numero = int(input('Digite um numero:\n'))

if numero == 10:
    print('Esse numero é igual a Dez')
elif numero > 10:
    print('Esse numero é maior a Dez')
else:
    print('Esse numero é menor que Dez')