# Faça um programa que peça ao usuário três números e verifique se todos são positivos.
num1 = int(input('Informe um numero \n'))
num2 = int(input('Informe mais um numero \n'))
num3 = int(input('Informe mais um numero \n'))
# Ainda fazer uma verificação 
if num3 < 0 or num2 < 0 or num1 < 0:
    print('Um desses são negativo')
else:
    print('Esses numero são positivo')