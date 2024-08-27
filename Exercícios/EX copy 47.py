# Crie um programa que peça ao usuário um número e exiba a tabuada desse número de 1 a 10.
num = int(input('informe uma tabuada'))

for count in range(10):
    print("%d x %d = %d" % (num, count+1, num*(count+1)) )
#print(num *1+1)