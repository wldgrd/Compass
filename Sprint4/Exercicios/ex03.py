'''A função calcula_saldo recebe uma lista de tuplas, correspondendo a um conjunto de lançamentos bancários. 
Cada lançamento é composto pelo seu valor (sempre positivo) e pelo seu tipo (C - crédito ou D - débito). 
Abaixo apresentando uma possível entrada para a função.

lancamentos = [
    (200,'D'),
    (300,'C'),
    (100,'C')
]
A partir dos lançamentos, a função deve calcular o valor final, somando créditos e subtraindo débitos. Na lista anterior, por exemplo, 
teríamos como resultado final 200.
Além de utilizar lambdas, você deverá aplicar, obrigatoriamente, as seguintes funções na resolução:

reduce (módulo functools)
map'''

from functools import reduce 

def calcula_saldo(lancamentos):
    #mapeando os valores de crédito e débito
    valores = map(lambda x: x[0] if x[1] == 'C' else -x[0], lancamentos)
    #usando o reduce para fazer o acumulador soma
    saldo_resultante = reduce(lambda soma, x: soma + x, valores)

    return saldo_resultante


