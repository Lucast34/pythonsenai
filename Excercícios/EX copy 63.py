# Desenvolva um algoritmo que peça ao usuário para inserir 5 números, adicione-os a uma lista e, depois, exiba a soma de todos os números na lista.
num_lis = []


for i in range(5):
    num = int(input('Digite cinco numero: '))
    num_lis.append(num)
    tt = sum(num_lis)
print(f'A soma desses numeros deu:{tt}')