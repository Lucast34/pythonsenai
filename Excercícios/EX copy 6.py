# Desenvolva um programa que pergunte ao usuário uma operação matemática (+, -, *, /) e dois números, e realize a operação escolhida.
operacao = str(input('Escolha uma operação:'))
numero =  int(input('escolha um numero: \n'))
numero2 =  int(input('escolha outro numero: \n'))
match operacao:
    case '+':
        print(numero + numero2 )
    case '-':
        print(numero - numero2)
    case '/':
        print (numero / numero2)
    case '*':
        print(numero * numero2)
