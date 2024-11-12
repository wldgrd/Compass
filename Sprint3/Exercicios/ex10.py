#Escreva uma função que recebe uma lista e retorna uma nova lista sem elementos duplicados. Utilize a lista a seguir para testar sua função.
#['abc', 'abc', 'abc', '123', 'abc', '123', '123']

def unicos(lista):
    return list(set(lista))

a = ['abc', 'abc', 'abc', '123', 'abc', '123', '123']
print(unicos(a))