nomes = []

#def cadastro ():
    #cadastro = input('seu nome por favor: ') 
    #nomes.append
    #return cadastro

operacao = 'sim'.lower() .strip()

while operacao == 'sim':
    print('1 cadastre nome ')
    print('2 atualize nome')
    print('3 Exclua')
    print('4 Listar')
    opcao=int(input('informe a ação desejada: '))
    match opcao:
        case 1:
            #cadastro
            nome = input('que nome você deseja cadastrar: ')
            nomes.append(nome)        
        case 2:
            print(opcao)
        case 3:
            print(opcao)
        case 4:
            for indice, nome in enumerate (nomes):
                print(nome)
        case _:
            print('opção invalida')

    operacao = input('Desejar realizr mais alguma operação? ').lower() .strip()

    if operacao != 'sim':
        break