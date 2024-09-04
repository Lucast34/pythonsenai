nomes = []


def cadastro(nome_nv,email ,data_nascimento, matricula):
    
    matricula += 1
    aluno = {'nome': nome_nv, 
    'email':email, 
    'data_nascimento': data_nascimento,
    'matricula': matricula
} 
    nomes.append(aluno)
    

def atualizar(nome_s, nome_update):
    nomes[nomes.index(nome_s)] =  nome_update
    

def excluir(nome_exclusão):
    nomes.remove(nome_exclusão)
    # nomes[nomes.remove(nome_exclusão)]

def listar():
    print(nomes)


def menu():
    opcoes =['Cadatrar nome', 'Atualizar nome', 'Excluir nome', 'Listar nomes']

    for indice, opcoes in enumerate(opcoes):
        print(f'{indice +1} - {opcoes}')
