import requests

cep = 7264000
link = f'http://viacep.com.br/ws/{cep}/json/' 

endereco = requests.get(link)

print(endereco)