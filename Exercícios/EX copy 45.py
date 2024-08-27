# Escreva um algoritmo que peça ao usuário para inserir 5 números e, ao final, exiba o maior número inserido
n1 = int(input('digite um numero:\n')) 
n2 = int(input('digite outro numero:\n'))
n3 = int(input('digite outro numero:\n'))
n4 = int(input('digite outro numero:\n'))
n5 = int(input('digite outro numero:\n'))

if n1 > n2:
    print('O primeiro numero é o maior')
elif n2 > n3:
    print('O segundo numero é o maior')
elif n3 > n4:
    print('O terceiro é o maior')
elif n4 > n5:
    print('O quarto é o maior')
else:
    print('O quinto é o maior')