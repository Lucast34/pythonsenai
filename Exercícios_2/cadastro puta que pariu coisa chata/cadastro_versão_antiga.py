nomes = ['Adriano']

def cadastro():
    nome_1 = input('seu nome por favor: ')
    nomes.append(nome_1)
    

def atualizar():
    nome_select =input('Qual nome que você deseja Mudar? ')
    nome_update = input(f'Qual será o novo nome?{nomes[nome_select]} ')
    #atualizado = input(f'Digite o valor para atualizar no item {nomes[val]}: ').strip().capitalize()
    nome_select =  nome_update
    

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
        case 2:
            atualizar()
            print('cadastro atualizado')
        case 3:
            excluir()
            print('cadastro excluido')
        case 4:
            listar()

        case _:
            print('opção invalida')

    operacao = input('Desejar realizr mais alguma operação? ').lower() .strip()

    if operacao != 'sim':
        break