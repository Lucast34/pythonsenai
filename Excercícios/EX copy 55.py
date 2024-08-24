# Desenvolva um programa que peça ao usuário para inserir um número maior que 100. Se o número for menor ou igual a 100, continue pedindo até que um número maior que 100 seja inserido.
nn = int(input('descubra a charada extremamente dificil (10*10+1):\n'))

while (nn >= 100):
    print('digite novamente')
    nn = int(input('Vamos lá você consegue:\n'))
    
print('parabêns você sabe matemśtica basica!')
