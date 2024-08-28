
from os import system



def cadastro ():
    system('clear')
    cadastro = input('seu nome por favor: ') 
    pessoa.append
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
    
    

menu_cadastro()

while True:
    opition = int(input('Digite um valor'))
    match opition:
        case 1:
            cadastro ()
        case 2:
            atualizar()
        case 3:
            excluir()
        case 4:
            lista()