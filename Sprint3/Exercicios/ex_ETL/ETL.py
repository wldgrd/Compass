#---------------------------------------------------------------------------------------------------------------------------------------

'''Apresente o ator/atriz com maior número de filmes e a respectiva quantidade. A quantidade de filmes encontra-se na coluna Number of 
    movies do arquivo.'''

#Leitura das linhas do arquivo
with open('C:\\Users\\welde\\OneDrive\\Documentos\\COMPASS UOL\\PB_Welder_Garrido\\Sprint3\\Exercicios\\ex_ETL\\actors.csv', 'r') as arquivo:
    linhas = arquivo.readlines()

#formatando o cabeçalho para o padrão nome_da_coluna
cabecalho = linhas[0].lower().replace(' ','_').strip().split(',')

#extração dos índices de cada coluna
print('Índices das colunas:')
for i,categoria in enumerate(cabecalho):
        print(f"Coluna {i} -> Título: {categoria}")

#colocando todas as informações em uma matriz, excluindo o cabeçalho
data = [ linha.strip().split(",") for linha in linhas[1:] ]

#---------------------------------------------------------------------------------------------------------------------------------------

#Etapa-1

'''Analisando os dados, encontrei um problema na linha de índice 4, onde o sobrenome Jr foi separado do nome e gerou uma coluna a mais'''

data[4] = ["Robert Downey Jr.", '3947.30 ',  '53',  '74.50 ', 'The Avengers', '623.40'] #Para corrigir o problema com o nome e das colunas
max_num = 0
ator = ""
for linha in data:
    num_filmes = int(linha[2]) #converte o campo Number of Movies para inteiro e atribui à variável num_filmes
    if num_filmes > max_num:
        max_num = num_filmes
        ator = linha[0] #extrai o nome do ator/atriz da linha que está sendo iterada, caso este tenha um número maior de filmes

print('\n#Etapa-1')
print(f"O ator com mais filmes é {ator} com um total de {max_num} filmes") #exibe o nome do ator e a quantidade de filmes

#---------------------------------------------------------------------------------------------------------------------------------------


#Etapa-2
'''Apresente a média de receita de bilheteria bruta dos principais filmes, considerando todos os atores. Estamos falando aqui da média 
    da coluna Gross'''

soma = 0
for linha in data:
    soma += float(linha[5]) #calcula a soma acumulada de todas as linhas da coluna Gross

media = soma/(len(data)) #calcula a média dividindo o valor da soma pela quantidade de itens, que corresponde ao número total de linhas da matriz data
print('\n#Etapa-2')
print(f'Média da receita bruta: {round(media,2)} milhões de dólares.')  #exibe a resposta do valor médio da receita bruta

#---------------------------------------------------------------------------------------------------------------------------------------

#Etapa-3
'''Apresente o ator/atriz com a maior média de receita de bilheteria bruta por filme do conjunto de dados. Considere a coluna Average 
    per Movie para fins de cálculo.'''

ator = ""
maximo = 0

for linha in data:
    receita_por_filme = float(linha[3])
    if receita_por_filme > maximo:
        maximo = receita_por_filme
        ator = linha[0]

print('\n#Etapa-3')
print(f'O ator com a maior média de receita de bilheteria bruta é {ator} com receita de {maximo} milhões de dólares.')

#---------------------------------------------------------------------------------------------------------------------------------------

#Etapa-4
'''A coluna #1 Movie contém o filme de maior bilheteria em que o ator atuou. Realize a contagem de aparições destes filmes no dataset,
   listando-os ordenados pela quantidade de vezes em que estão presentes. Considere a ordem decrescente e, em segundo nível, o nome do filme.
    Ao escrever no arquivo, considere o padrão de saída (sequência) - O filme (nome do filme) aparece (quantidade) vez(es) no dataset, 
    adicionando um resultado a cada linha.'''

lista_filmes = [linha[4] for linha in data] #lista com os filmes e suas repetições
filmes = set([linha[4] for linha in data]) #filmes únicos

cont =  []
for filme in filmes:
    cont.append([filme, lista_filmes.count(filme)])

conteudo_ordenado = sorted(cont, key = lambda x: (-x[1], x[0]))

print('\n#Etapa-4')
for i, (filme, cont) in enumerate(conteudo_ordenado, start = 1):
    print(f'({i}) - O filme {filme} aparece {cont} vez(es) no dataset.') 

#---------------------------------------------------------------------------------------------------------------------------------------

#Etapa-5
'''Apresente a lista dos atores ordenada pela receita bruta de bilheteria de seus filmes (coluna Total Gross), em ordem decrescente.
Ao escrever no arquivo, considere o padrao de saída (nome do ator) - (receita total bruta), adicionando um resultado a cada linha.'''

ator_receita = []
for linha in data:
    ator_receita.append([linha[0], float(linha[1])])

ator_receita_ordenado = sorted(ator_receita, key = lambda x: (-x[-1], x[0]))

print('\n#Etapa-5')
for linha in ator_receita_ordenado:
    print(f'{linha[0]} - {linha[1]} milhões de dólares')

#---------------------------------------------------------------------------------------------------------------------------------------