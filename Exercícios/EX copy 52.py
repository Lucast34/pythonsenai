# Desenvolva um algoritmo que solicite ao usuário uma senha e continue pedindo até que a senha correta "1234" seja digitada.
s = 1234
t = int(input('Descubra a senha:\n'))
while (s != t):
    print('tente novamente')
    t = int(input('descubra a senha:\n'))
print('Senha correta parabêns!!!!!!')