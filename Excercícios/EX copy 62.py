# Escreva um programa que solicite ao usuário para inserir 3 nomes e armazene-os em uma lista. Em seguida, imprima a lista completa.

nlist = []

for i in range(3):
    n = str(input('digite três nomes:'))
    nlist.append(n)

print(nlist)