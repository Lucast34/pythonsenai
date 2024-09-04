from ast import Num


num_sum = int()

for i in range(1, 11):
    num = int(input(f'Digite o numero {i}: '))
    num_sum += num

media = num_sum / 10
print('A media é: ', media)