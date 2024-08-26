# Desenvolva um algoritmo que pergunte ao usuário o nome de uma cidade e verifique se é a capital do Brasil.
c = 'distrito federal'
t = str(input('Digite um estado: '))

while t != c:
    print('Não é a capital do Brasil')
    t = str(input('Digite um estado: '))
print('É a capital do Brasil')