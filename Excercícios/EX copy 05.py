# Faça um programa que solicite ao usuário dois números e verifique se ambos são pares.
numero = int(input('escolha um numero: \n'))
numero2 = int(input('escolha outro numero: \n'))

if numero % 2 == 0 and numero2 % 2 == 0:
    print( 'os numeros são pares')
else:
    print('um dos numeros não são pares')