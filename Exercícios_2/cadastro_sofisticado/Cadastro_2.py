from os import system
import funcoes_cadastro as mo

operacao = 'sim'.lower() .strip()
matricula = 1
while operacao == 'sim':
    mo.menu()
    opcao = int(input('Selecione uma opção '))
    match opcao:
        case 1:
            nome_nv = input('Nome do aluno: ')
            email = input('O email do aluno: ')
            data_nascimento = input('')
            matricula+=1
            mo.cadastro(nome_nv, email, data_nascimento,matricula)
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

