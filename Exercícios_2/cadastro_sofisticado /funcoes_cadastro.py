nomes = []
email = []
numero_matricula = []
data_nascimento = []

def cadastro(nome_nv):
    nomes.append(nome_nv)
    

def atualizar(nome_s, nome_update):
    nomes[nomes.index(nome_s)] =  nome_update
    

def excluir(nome_exclusão):
    nomes.remove(nome_exclusão)
    # nomes[nomes.remove(nome_exclusão)]

def listar():
    


def menu():
    opcoes =['Cadatrar nome', 'Atualizar nome', 'Excluir nome', 'Listar nomes']

    for indice, opcoes in enumerate(opcoes):
        print(f'{indice +1} - {opcoes}')
