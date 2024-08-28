# Escreva um algoritmo que forneça um menu para o usuário: 1-Cadastrar nome, 2- atualizar o nome, 3, excluir, 4-listar todos os cadastrados, ao final da operação deve dar uma mensagem indicando o resultado da operação e perguntando se deseja realizar
# outra operação, o seu aplicativo apenas deve encerrar quando a opção não for inserida.
import os

def cadastro ():
    os.system ('clear')
    cadastro = input('Qual é o seu nome ?')
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

pessoa = ['nome:']


print ('O quê você deseja fazer ?(Aperte 0 se quer sair do programa)')
print ('1- Cadastrar um nome')
print ('2- Atualizar o nome')
print ('3- Excluir')
print ('4- Listar todo os casdastados')

selecao = input('Insira a opção: ')

while True:
    match selecao:
        case 1:
            cadastro()
        case 2:
            atualizar ()
        case 3:
            excluir()
        case 4:
            lista()
