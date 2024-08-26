#  exemplos usando cavaleiros 
# from operator import index


# cavaleiros = ['Senya', 'Shun', 'Shiryu', 'Yoga', 'Aldebaran', 'Aldebaran']

# print(cavaleiros)

# # adiciona um novo elemento ao final da lista
# cavaleiros.append('Ikki')
# print(cavaleiros)

# # extendendo a lista con outra lista
# cavaleiros.extend(['Shina','Maryn'])
# print(cavaleiros)

# # inserir na lista em uma posição espercifica
# cavaleiros.insert(0,'Athena')
# print(cavaleiros)

# # remove, exclui um elemento pelo valor.
# cavaleiros.remove('Shun')
# print(cavaleiros)

# # pop - exclui o ultimo elmrnto da lista ou o indice informado
# elemento = cavaleiros.pop
# print(elemento)
# cavaleiros.pop()
# print(cavaleiros)

# cavaleiros.pop(0)
# print(cavaleiros)

# #indice (só em string e em lista) // retorna o indice da primeira ocorrencia de um valo procurado
# print(cavaleiros.index('Yoga')) 

# cavaleiros.pop(cavaleiros.index('Yoga'))
# print(cavaleiros)

# # alterando valo de um elemento 
# cavaleiros[cavaleiros.index('Ikki')] = 'Ikki de fenix'
# print(cavaleiros)

# #contabilizando quantidade de elementos repetidos
# print(cavaleiros.count('Aldebaran'))

# sort ordena a lista de forma crescente
frutas = ['morango', 'maçã', 'abacaxi', 'kiwi', 'amora', 'umbu', 'laranja', 'bergamota']

num = [4,888,1616,9999999,10,2,4,6,7,54]

frutas.sort()
num.sort()

print(frutas)
print(num)

frutas.reverse()
num.reverse()

print(frutas)
print(num)

del frutas[0]
print(frutas)

frutas.clear()
print(frutas)

del frutas
print(frutas)