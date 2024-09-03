# 10 informaçôes pessoais de cadastro e informe um relatorio com as informações em um unico print 

nome = input('informe seu nome: ')
idade = int (input('Informe o sua idade: ')) 
cpf = int (input('Informe o seu CPF: '))
casa = input ('Possui casa propia: ')
cateira_de_motorista = input ('Possui carteira de motorista:')
animal = (input('Possui animal de estimação: '))
crenca = input('Possui uma crença: ')
signo = input('Qual é o seu signo: ')
endereco = input('Qual é o seu endereço: ')
formacao = input ('Qual é a sua Formaçâo: ')

print (f'Prazer {nome}, sou seu assistente, estou vendo que você possui {idade} anos, seu cpf é {cpf}, \
      você {casa} possui uma casa própria, {animal} você tem um animal de estimção, você é {crenca} \
        legal você mora em {endereco}, e você possui o signo {signo} e você é formado em {formacao}')