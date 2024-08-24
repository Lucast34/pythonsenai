# Crie um algoritmo que solicite ao usuário um número e continue pedindo outro número até que um número negativo seja inserido.

nn = int(input('Insira um numero um negativo:\n'))

while (nn > 0):
    print('digite novamente')
    nn = int(input('Insira um numero um negativo:\n'))
    
print('parabêns você sabe ler!')
