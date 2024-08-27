# Escreva um programa que solicite ao usuário para digitar dois números e verifique se o primeiro é maior que o segundo. Continue pedindo números até que o primeiro número seja maior que o segundo
p = int(input('digite um numero:\n'))
s = int(input('digite outro numero:\n'))

while p < s:
    print('o primeiro tem que ser maior que o segundo ')
    p = int(input('digite um numero:\n'))
    s = int(input('digite outro numero:\n'))

print('IHAAAAAAAAAAAAAAAAAAAAA!')