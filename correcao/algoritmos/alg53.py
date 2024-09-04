from os import system
import time

num = int(input('Digite um numero: '))


while num >= 1:
    system('clear')
    print(num)
    num -= 1 
    time.sleep(1)