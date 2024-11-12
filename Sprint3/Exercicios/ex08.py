# Verifique se cada uma das palavras da lista ['maça', 'arara', 'audio', 'radio', 'radar', 'moto'] é ou não um palíndromo.
# Obs: Palíndromo é uma palavra que permanece igual se lida de traz pra frente.
# É necessário que você imprima no console exatamente assim:
# A palavra: maça não é um palíndromo
# A palavra: arara é um palíndromo
# A palavra: audio não é um palíndromo
# A palavra: radio não é um palíndromo
# A palavra: radar é um palíndromo
# A palavra: moto não é um palíndromo

palavras = ['maça', 'arara', 'audio', 'radio', 'radar', 'moto']
invertidas = []
for palavra in palavras:
    invertidas.append(palavra[::-1])

for i in range(len(palavras)):
    if palavras[i] == invertidas[i]:
        print("A palavra:", palavras[i], "é um palíndromo")
    else:
        print("A palavra:", palavras[i], "não é um palíndromo")