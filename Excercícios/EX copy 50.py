# Crie um programa que peça ao usuário para inserir um número e, em seguida, exiba os números de 1 até esse número, mas de forma decrescente.
n = int(input('digite um numero:\n'))

for i in range(n,0, -1):
    print(i)
