# Crie um programa que solicite ao usuário três números e exiba o maior deles.
n1 = int(input('digite um numero:\n')) 
n2 = int(input('digite outro numero:\n'))
n3 = int(input('digite outro numero:\n'))

if n1 > n2:
    print('O primeiro numero é o maior')
elif n2 > n3:
    print('O segundo numero é o maior')
else:
    print('O tericeiro é o maior')
