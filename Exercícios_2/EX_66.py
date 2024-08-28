# Escreva um algoritmo que forneça um menu para o usuário: 1-Cadastrar nome, 2- atualizar o nome, 3, excluir, 4-listar todos os cadastrados, ao final da operação deve dar uma mensagem indicando o resultado da operação e perguntando se deseja realizar
# outra operação, o seu aplicativo apenas deve encerrar quando a opção não for inserida.

def cadastro ():
    cadastro = pessoa.append('nome: ')
    return cadastro

def atualizar ():
    atualizar = print()
    return atualizar

def excluir ():
    excluir = print()
    return excluir

def lista ():
    lista = print()
    return lista

pessoa = []

def menu_cadastro():
    print ('O quê você deseja fazer ?(Aperte 0 se quer sair do programa)')
    print ('1- Cadastrar um nome')
    print ('2- Atualizar o nome')
    print ('3- Excluir')
    print ('4- Listar todo os casdastados')
    selecao = input('Insira a opção: ')
    return selecao

print(menu_cadastro)
