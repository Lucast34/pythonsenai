# Desenvolva um algoritmo que peça ao usuário para digitar dois números e verifique se a multiplicação deles é igual a 20.
n1 = int(input('digite um numero:\n')) 
n2 = int(input('digite outro numero:\n'))

if n1 * n2 == 20:
    print('Essa operação deu 20')
else:
    print ('Essa operação não deu 20')