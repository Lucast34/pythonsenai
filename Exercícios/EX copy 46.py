# Desenvolva um programa que pergunte ao usuário para inserir 10 números e, ao final, exiba a média dos números inseridos.
num_list = []
for i in range(10):
    num = int(input('digite dez numeros:\n'))
    num_list.append(num)

med = sum(num_list)/10
print('A média dos números é :', med)
