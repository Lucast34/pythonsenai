# Crie um programa que peça ao usuário para adivinhar um número secreto entre 1 e 10. Continue pedindo até que ele adivinhe o número corretamente.
s = 8
t = int(input('adivinhe a senha:\n'))

while t != s:
    print('tente novamente!!!')
    t = int(input('adivinhe a senha:\n'))

print('parabêns você acertou!')