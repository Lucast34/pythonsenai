#  Escreva um programa que pergunte ao usuário quantas vezes ele quer que uma mensagem seja exibida, e utilize um laço while para exibir a mensagem a quantidade de vezes desejada.
c = 0
t = int(input('quantas vezes:'))

while t > c:
    c += 1
    print(f'contagem {c}')