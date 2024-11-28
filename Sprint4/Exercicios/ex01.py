'''Você está recebendo um arquivo contendo 10.000 números inteiros, um em cada linha. 
Utilizando lambdas e high order functions, apresente os 5 maiores valores pares e a soma destes.
Você deverá aplicar as seguintes funções no exercício:
map
filter
sorted
sum
Seu código deverá exibir na saída (simplesmente utilizando 2 comandos `print()`):
a lista dos 5 maiores números pares em ordem decrescente;
a soma destes valores.'''

numeros = [int(linha.strip()) for linha in open('number.txt')]
pares_ordenados = sorted(list(filter(lambda n: n%2 == 0, numeros)), reverse = True)
maiores = list(map(int,pares_ordenados[:5]))
soma = sum(maiores)

print(maiores)
print(soma)