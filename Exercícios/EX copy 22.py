# Escreva um programa que peça ao usuário para inserir dois números e verifique se o primeiro é maior que o segundo.
numero = int(input('Digite um numero:\n'))
numero2 = int(input('Digite outro numero:\n'))

if numero > numero2:
    print('O primeiro é maior que segundo')
elif numero < numero2:
    print('O segundo é maior que primeiro')
else:
    print('Esses numero são iguais')