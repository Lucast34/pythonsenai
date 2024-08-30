#exercicio_66


from os import system
# import modulo
# from modulo import menu,listar
import modulo as mo

operacao = 'sim'.lower() .strip()

while operacao == 'sim':
    mo.menu()
    opcao = int(input('Selecione uma opção '))
    match opcao:
        case 1:
            nome_nv = input('seu nome por favor: ')
            mo.cadastro(nome_nv)
            print('cadastro adicionado')    
        case 2:
            nome_s = input('Qual nome que você deseja Mudar? ')
            nome_update = input('qual será o novo nome')
            mo.atualizar(nome_s, nome_update)
            print('cadastro atualizado')
        case 3:
            nome_exclusão = input('Qual nome você quer excluir? ')
            mo.excluir(nome_exclusão)
            print('cadastro excluido')
        case 4:
            mo.listar()
        case _:
            print('opção invalida')

    operacao = input('Desejar realizr mais alguma operação? ').lower() .strip()
    system('clear')
    
    if operacao != 'sim':
        break
