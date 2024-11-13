'''Imprima a lista abaixo de trás para frente.

a = [1, 0, 2, 3, 5, 8, 13, 21, 34, 55, 89]'''

a = [1, 0, 2, 3, 5, 8, 13, 21, 34, 55, 89]

inicio = len(a) - 1 

b = []

for i in range(inicio, -1, -1):
    b.append(a[i])
    
print(b)