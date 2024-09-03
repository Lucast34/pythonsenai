# calcular o delta da formula de bhaskara 

from math import pow

Val_a =  float(input('informe o valor A'))
Val_b =  float(input('informe o valor B'))
Val_c =  float(input('informe o valor C'))

print(f'o valor de Delta é: {(pow(Val_b,2)-4 * Val_a * Val_c)}')