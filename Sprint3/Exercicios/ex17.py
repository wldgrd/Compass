'''Escreva uma função que recebe como parâmetro uma lista e retorna 3 listas: 
a lista recebida dividida em 3 partes iguais. Teste sua implementação com a lista abaixo

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]'''

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

def split_list(lista):
    terco = len(lista)//3
    lista1 = lista[0:terco]
    lista2 = lista[terco: 2*terco]
    lista3 = lista[2*terco:]
    
    return lista1, lista2, lista3
    
r1, r2, r3 = split_list(lista)
print(r1, r2, r3)