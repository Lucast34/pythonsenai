# numeros = [1, 5 , 8, 10, 9, 3, 368, 100, 51]
# # ver o maior
# print(max(numeros))
# # ver o menor
# print(min(numeros))
# # retorna a quantidade dentro da lista
# print(len(numeros))
# # soma todos os elementos da lista
# print(sum(numeros))

# media = sum(numeros) / len(numeros)

# print(media)

# # função
# def media (numeros):
#     soma = sum(numeros) / len(numeros)
#     return soma     
    

# print(media(numeros))

# # função com retorno
# def soma (numeros):
#     res = sum(numeros)
#     return res

# resp = soma(numeros)
# print(resp)

# # função sem retorno
# def saudacao(nome):
#     print(f'Hello {nome}')

# # uso da função
# saudacao('Luy')

# # função com paramentro opcional
# def ola(nome, mensagem='Olá'):
#     print(mensagem , nome)

# ola('Luy')

# função com multiplo retorno

# def dividir (n1, n2):
#     res = n1 // n2
#     resto = n1 % n2
#     return res, resto

# divisao, resto_divicao = dividir(0, 2)
# print(divisao, resto_divicao)  

# caso de tuple
# divisao = dividir(10, 2)
# print(divisao)  
# outro caso de tuple
# numeros = (1, 5 , 8, 10, 9, 3, 368, 100, 51)
# print(type(numeros))


# simplificador de funções 
# def soma (a, b):
#      soma = a + b
#      return soma

# somar = lambda a, b: a + b

# print(somar(10,5))


# def exibir_info (*args):
#     print('Argumentos posicionais: ', args)
    

# exibir_info(1,4,'Luy')

# def exibir_info2 (**args):
#     print('Argumentos posicionais: ', args)
    
# exibir_info2(nome='Luy', idade =20, curso='python')


# dicionario
# key:chave
#value:valor
# pessoa1 ={
#     'nome':'Luy',
#     'idade': 20,
#     'estado_civil':'solteiro',
#     'escolaridade': 'cursando'
# },
# pessoa2 ={
#     'nome':'Daniel',
#     'idade': 19,
#     'estado_civil':'noivo',
#     'escolaridade': 'cursando'
# },
# pessoas =[{
#     'nome':'Luy',
#     'idade': 20,
#     'estado_civil':'solteiro',
#     'escolaridade': 'cursando'
# },
# {
#     'nome':'Daniel',
#     'idade': 19,
#     'estado_civil':'noivo',
#     'escolaridade': 'cursando'
# },]

# print(pessoas[1])