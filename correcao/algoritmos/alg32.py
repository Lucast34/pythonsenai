palindromo = input('informe a sua frase: ').lower().strip()

if palindromo == palindromo[::-1]:
    print('é palindromo')
else:
    print('não é palindromo')
