'''Escreva uma função que recebe um número variável de parâmetros não nomeados 
e um número variado de parâmetros nomeados e imprime o valor de cada parâmetro recebido.
Teste sua função com os seguintes parâmetros:
(1, 3, 4, 'hello', parametro_nomeado='alguma coisa', x=20)'''

def func(*nao_nomeados, **nomeados):
    #print('Não nomeados: ', len(nao_nomeados))
    for valor in nao_nomeados:
        print(valor)

    
    #print('Nomeados: ', len(nomeados))
    for chave, valor in nomeados.items():
        print(f'{valor}')

func(1, 3, 4, 'hello', parametro_nomeado='alguma coisa', x=20)