# Crie um programa que peça ao usuário um número inteiro positivo e exiba todos os números de 1 até o número informado
n1 = int(input('digite um numero:\n')) 

if n1 < 0:
    print('apenas numeros positivos')
for n1 in range(1,n1 + 1):
    print(n1)