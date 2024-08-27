#Escreva um programa que peça ao usuário para digitar sua altura em metros e verifique se ela é maior que 1.75.

al1 = float(input('digite sua altura:\n'))

if al1 >1.75:
    print('você é maior que a média')
elif al1 >= 1.65:
    print('você esta na média')
else:
    print('você é baixo')