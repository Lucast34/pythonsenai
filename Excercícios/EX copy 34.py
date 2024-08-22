# Escreva um programa que peça ao usuário um número e verifique se ele é positivo, negativo ou zero.
n1 = int(input('Digite um numero\n'))

if n1 > 0:
    print('esse numero é positivo')
elif n1 == 0:
    print('esse numero é igual a zero')
else:
    print('esse numero é negativo')