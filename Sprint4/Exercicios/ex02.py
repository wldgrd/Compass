'''Utilizando high order functions, implemente o corpo da função conta_vogais.
O parâmetro de entrada será uma string e o resultado deverá ser a contagem de vogais presentes em seu conteúdo.

É obrigatório aplicar as seguintes funções:
len
filter
lambda
Desconsidere os caracteres acentuados. Eles não serão utilizados nos testes do seu código.'''

def conta_vogais(texto:str)-> int:
    lista_vogais = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    lista_caracteres = list(map(lambda x: x, texto))
    vogais = list(filter( lambda d: d in lista_vogais, lista_caracteres ))
    qtd_vogais = len(vogais)
    return qtd_vogais