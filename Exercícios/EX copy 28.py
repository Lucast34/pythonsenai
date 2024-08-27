# Escreva um programa que peça ao usuário para inserir uma palavra e verifique se ela tem mais de 5 letras.
nome = str(input('Digite o seu nome:\n'))

print(len(nome))

if len(nome)> 5:
    print('Esse nome tem mais cinco letras')
else:
    print('esse nome tem menos de cinco de letras')