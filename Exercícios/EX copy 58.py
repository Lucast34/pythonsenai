# Desenvolva um algoritmo que solicite ao usuário uma palavra e continue pedindo outra palavra até que ele digite "sair".
s = 'sair'
t = str(input('adivinhe a senha:\n'))
while t != s:
    print('tente novamente!!!')
    t = str(input('adivinhe a senha:\n'))

print('parabêns você acertou!')