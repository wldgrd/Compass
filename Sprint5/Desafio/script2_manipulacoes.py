import pandas as pd

#Leitura dos dados do arquivo .csv
df = pd.read_csv('dataset-baixado.csv') 

#fazendo uma cópia de segurança
df1 = df.copy()
dim_inicial = df1.shape

print('+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-INÍCIO-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+')

#verificando as dimensões do dataset original
print('As dimensões do dataset original são: ',dim_inicial)

#derrubando todas as linhas que possuem pelo menos um valor NaN
df1 = df1.dropna()
dim_final = df1.shape

#salvando o dataset limpo
df_limpo = df1 
df_limpo.to_csv('./df_limpo.csv', index=False)
print('Dataset limpo salvo com sucesso.')
print()
print('+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+')


#verificando novamente as dimensões do dataset, agora pós modificação
print('As novas dimensões do dataset são:' ,dim_final)

#Calculando a quantidade de linhas deletadas por possuirem valores NaN
print('A quantidade de linhas deletadas foi de: ', (dim_inicial[0] - dim_final[0]))
print('+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+')
#verificando o cabeçalho do dataset
print()
print('Visualização das 10 primeiras linhas do dataset: ')
print(df1.head(10))
print('+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+')

#verificando os tipos de dados de cada coluna
print()
print('Verificação dos tipos de cada coluna', df1.dtypes)
print()
print()
print('+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+')

#Conversão das colunas de data de início e fim da certificação para tipo data.
df1['cebas_dt_inicio_certificacao_s'] = pd.to_datetime(df1['cebas_dt_inicio_certificacao_s'], format = '%d/%m/%Y')
df1['cebas_dt_fim_certificacao_s'] = pd.to_datetime(df1['cebas_dt_fim_certificacao_s'], format = '%d/%m/%Y')

print()
print('Os tipos depois da conversão são: ',df1.dtypes)
print()
print('+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+')

# 4.1 - Filtrar dados usando dois operadores lógicos

#selecionando as entidades com status de certificação vigente ou válidae que contenham hospital ou alguma variação disso no nome
#criação de um dataframe auxiliar para gravar o subconjunto de dados correspondente ao filtro aplicado
print()
df_aux = df1[
    ((df1['cebas_status_certificacao_s'] == 'VIGENTE') | (df1['cebas_status_certificacao_s'] == 'VÁLIDA' )) & (df1['cebas_razao_social_entidade_s'].str.contains(r'HOSPITAL'))
].reset_index(drop = True) #reset_index(drop=True) para resetar os índices do novo dataframe e derrubar os índices usados anteriormente
print('Filtrando entidades com status de certificação vigente ou válida e que contenham Hospital no nome.')
print(df_aux.head(10))
print('+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+')
print()


# Calcular a duração da certificação em dias (utilizando vetorização)

print('Inserida a coluna de duração da certificação (dias)')
df_aux['duracao_dias'] = (df_aux['cebas_dt_fim_certificacao_s'] - df_aux['cebas_dt_inicio_certificacao_s']).dt.days #subtração das datas e conversão para dias
print(df_aux)
print()
print('+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+')


# 4.5 - Filtrar para certificações que começaram em 2021
print()
print('Filtrando pelas certificações iniciadas em 2021')
df_aux = df_aux[df_aux['cebas_dt_inicio_certificacao_s'].dt.year == 2021]

print(df_aux)
print()
print('+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+')


# 4.2 - Aplicar agregações: contar total de entidades e somar por status

print()
agregacoes = df_aux.groupby('cebas_status_certificacao_s').agg(total=('cebas_razao_social_entidade_s', 'count')).reset_index() #faz a contagem e mostra o valor numa coluna renomeada para 'total'
print('Contagem de entidades por status de certificação.')
print(agregacoes)
print()
print('+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+')

# 4.6 - Converter o nome das entidades para primeira letra maiúscula e as demais minúsculas
print()
df_aux['cebas_razao_social_entidade_s'] = df_aux['cebas_razao_social_entidade_s'].str.capitalize()
print(df_aux['cebas_razao_social_entidade_s'])
print()
print('+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+')

print()
df_aux.to_csv('./df_aux.csv', index = False)
print('Arquivo df_aux.csv salvo com sucesso.')
agregacoes.to_csv('./agregacoes.csv', index = False)
print('Arquivo agregacoes.csv salvo com sucesso.')
