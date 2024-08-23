maior = None

for i in range(5):
    num = int(input(f'informe o numero {i+1}:'))

    if maior is None or num > maior:
        maior = num


print(f'O maior numero é:{maior}')
















# maior = 0

# for i in range(5):
#     num = int(input(f'informe o numero {i+1}'))

#     if num > maior:
#         maior = num


# print(f'O maior numero é:{maior}')