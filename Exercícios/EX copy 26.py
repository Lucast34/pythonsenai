# Desenvolva um algoritmo que peça ao usuário para inserir dois números e verifique se ambos são múltiplos de 5.
numero = int(input('Digite um numero:\n'))
numero2 = int(input('Digite outro numero:\n'))

if numero % 5 == 0 and numero2 % 5 == 0:
    print('ambos são múltiplo de 5')
else:
    print('um dos numeros não é múltiplo de 5')
