'''Escreva uma função que recebe uma string de números separados por vírgula e retorne a soma de todos eles. Depois imprima a soma dos valores.

A string deve ter valor  "1,3,4,6,10,76"'''

string = "1,3,4,6,10,76"
numeros = string.split(',')

soma = 0

for numero in numeros:
    soma = soma + int(numero)

print(soma)