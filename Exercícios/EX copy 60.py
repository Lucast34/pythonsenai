# Crie um programa que peça ao usuário um número e exiba todos os divisores desse número.
n = int(input('Digite o numero que você quer descobrir os divisores:'))

for i in range(n):

    if n %(i +1) == 0:
        print(i + 1)

