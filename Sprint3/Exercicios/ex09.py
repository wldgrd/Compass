''' Dada as listas a seguir:
 primeirosNomes = ['Joao', 'Douglas', 'Lucas', 'José']
 sobreNomes = ['Soares', 'Souza', 'Silveira', 'Pedreira']
 idades = [19, 28, 25, 31]
 Faça um programa que imprima o dados na seguinte estrutura: "índice - primeiroNome sobreNome está com idade anos".
 Exemplo:
 0 - João Soares está com 19 anos'''

primeirosNomes = ['Joao', 'Douglas', 'Lucas', 'José']
sobreNomes = ['Soares', 'Souza', 'Silveira', 'Pedreira']
idades = [19, 28, 25, 31]

for i, (primeirosNomes, sobreNomes, idades) in enumerate(zip(primeirosNomes, sobreNomes, idades)):
    print(i, '-' , primeirosNomes, sobreNomes, 'está com', idades, 'anos')