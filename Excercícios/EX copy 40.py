# Escreva um programa que peça ao usuário para inserir três números e verifique se todos são iguais.
n1 = int(input('digite um numero:\n')) 
n2 = int(input('digite outro numero:\n'))
n3 = int(input('digite outro numero:\n'))

if n1 == n2 and n2 == n3:
    print('Os numeros são iguais')
else:
    print('Os numeros não são iguais')
