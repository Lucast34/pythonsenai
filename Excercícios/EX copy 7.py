# Escreva um programa que peça ao usuário uma nota de 0 a 10 e classifique a nota como "Baixa", "Média" ou "Alta" usando estrutura condicional if.
nota = int(input('Digite uma nota: \n'))

if (nota <= 5):
    print('Baixa')
elif(nota == 6):
    print('Média')
else:
    print('Alta')
