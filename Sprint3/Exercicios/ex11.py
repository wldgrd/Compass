'''Leia o arquivo person.json, faça o parsing e imprima seu conteúdo.

Dica: leia a documentação do pacote json'''

import json

'''arquivo = open('person.json', 'r')
conteudo = json.load(arquivo)
arquivo.close()

print(conteudo)'''

with open('person.json', 'r') as arquivo:
    conteudo = json.load(arquivo)
print(conteudo)