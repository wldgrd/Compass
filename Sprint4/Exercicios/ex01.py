numeros = [int(linha.strip()) for linha in open('number.txt')]
pares_ordenados = sorted(list(filter(lambda n: n%2 == 0, numeros)), reverse = True)
maiores = list(map(int,pares_ordenados[:5]))
soma = sum(maiores)

print(maiores)
print(soma)