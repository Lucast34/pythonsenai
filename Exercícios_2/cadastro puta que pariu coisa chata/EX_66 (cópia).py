nomes = ['Adriano']

def cadastro():
    nome_1 = input('seu nome por favor: ')
    nomes.append(nome_1)
    

def atualizar():
    for indice,nomes in enumerate(nomes):
    nome_select = input('Qual nome que você deseja Mudar? ')
    nome_update = nomes.index(input('Qual será o novo nome? '))
    #nomes.index(nome_update)
    

def excluir():
    nome_exclusão = input('Qual nome você quer excluir? ')
    nomes.remove(nome_exclusão)
    # nomes[nomes.remove(nome_exclusão)]

def listar():
    print(nomes)

operacao = 'sim'.lower() .strip()

while operacao == 'sim':
    print('1 cadastre nome ')
    print('2 atualize nome')
    print('3 Exclua')
    print('4 Listar')
    opcao=int(input('informe a ação desejada: '))
    match opcao:
        case 1:
            cadastro()
            print('cadastro adicionado')
            
            # nome = input('que nome você deseja cadastrar: ')
            # nomes.append(nome)        
        case 2:
            atualizar()
        case 3:
            excluir()
        case 4:
            listar()

        case _:
            print('opção invalida')

    operacao = input('Desejar realizr mais alguma operação? ').lower() .strip()

    if operacao != 'sim':
        break