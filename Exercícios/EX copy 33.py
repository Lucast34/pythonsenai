# Crie um programa que solicite ao usuário o valor de um produto e calcule o desconto de 10%.
pr1 = int(input('Qual é o preço do produto?\n'))
des = int(input('Quanto é o desconto ? \n'))
preco = (pr1 * des /100)


print(f'valor do desconto é {preco}')