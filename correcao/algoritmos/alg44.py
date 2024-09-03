num_list = list()

for i in range(10):
    num = int(input('Digite um número: '))
    if num % 2 == 0:
        num_list.append(num)

print('osnumeros pares sâo:', sorted(num_list))
