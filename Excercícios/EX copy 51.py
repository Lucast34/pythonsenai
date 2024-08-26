# Crie um programa que peça ao usuário para inserir números até que ele digite o número 0. Ao final, exiba a soma de todos os números inseridos (exceto o 0).
num_list = []

for i in range(5):
    num = int(input('digite cinco numeros:\n'))
    num_list.append(num)
    
r = sum(num_list)
    

print(r)