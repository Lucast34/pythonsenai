# Escreva um algoritmo que solicite ao usuário 5 números inteiros e calcule a soma desses números
n1 = int(input('digite um numero:\n')) 
n2 = int(input('digite outro numero:\n'))
n3 = int(input('digite outro numero:\n'))
n4 = int(input('digite outro numero:\n'))
n5 = int(input('digite outro numero:\n'))

if n1 < 0 or n2 < 0 or n3 < 0 or n4 < 0 or n5 < 0: 
    print('APENAS NUMEROS INTEIROS E POSITIVOS')
else:
    print (n1+n2+n3+n4+n5)