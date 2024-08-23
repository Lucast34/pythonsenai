# Escreva um programa que peça ao usuário um número e exiba a contagem regressiva desse número até 1.
n = int(input('digite um numero:\n'))

for i in range(n,0, -1):
    print(i)