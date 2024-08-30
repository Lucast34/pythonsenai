import os

nomes = ['Adriano']

def cadastro():
    nome_1 = input('seu nome por favor: ')
    nomes.append(nome_1)
    

def atualizar():
    nome = input('Qual nome que você deseja Mudar? ')
    nome_update = input('qual será o novo nome')
    #atualizado = input(f'Digite o valor para atualizar no item {nomes[val]}: ').strip().capitalize()
    nomes[nomes.index(nomes)] =  nome_update
    

def excluir():
    nome_exclusão = input('Qual nome você quer excluir? ')
    nomes.remove(nome_exclusão)
    for nomes
    # nomes[nomes.remove(nome_exclusão)]

def listar():
    for indice, nome in enumerate(nomes):
        print(f'{indice +1} - {nome}')

operacao = 'sim'.lower() .strip()

def menu():
    opcoes =['Cadatrar nome', 'Atualizar nome', 'Excluir nome', 'Listar nomes']

    for indice, opcoes in enumerate(opcoes):
        print(f'{indice +1} - {opcoes}')

while operacao == 'sim':
    menu()
    opcao = input('Selecione uma opção ')
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
    os.system('clear')
    
    if operacao != 'sim':
        break
