# Escreva um programa que pergunte ao usuário uma idade e verifique se a pessoa é adolescente (entre 13 e 19 anos).
idade = int(input('Digite a sua idade:\n'))

if idade > 12 and idade <= 17:
    print ('Você é um adolescente')
elif idade > 18:
    print ('Você é um adulto')
else:
    print ('Você é uma criança ')
    