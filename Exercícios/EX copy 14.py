# Desenvolva um algoritmo que peça ao usuário para digitar dois números e verifique se a soma deles é maior que 100.
numero = int(input('Digite um numero: \n'))
numero2 = int(input('Digite outro numero: \n'))

if numero + numero2 > 100:
    print('A soma desse dois numeros é maior que 100')
else:
    print('A soma dessse numeros não é maior que 100')