#Escreva um código Python que use a função range() para adicionar três números em uma lista(Esta lista deve chamar-se 'números')  e 
# verificar se esses três números são pares ou ímpares. Para cada número, imprima como saída Par: ou Ímpar: e o número correspondente (um linha para cada número lido).
#Importante: Aplique a função range() em seu código.
#Exemplos de saída:
#Par: 2
#Ímpar: 3

numeros = list(range(4,7))

for num in numeros:
    if num%2 == 0:
        print('Par:', num)
    else:
        print('Ímpar:', num )