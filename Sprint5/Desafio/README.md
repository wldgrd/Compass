# Objetivo  
O objetivo é praticar os conhecimentos da AWS.

# Instruções Gerais do Desafio  
**1**. Procure um arquivo CSV ou JSON no portal de dados públicos do Governo Brasileiro http://dados.gov.br
			- Garanta que seu arquivo seja único na sua turma.
			
**2**. Analise o conjunto de dados escolhido localmente em editor de texto de sua preferência
		para você conhecer os dados e o que pode ser analisado.
	
**3**. A partir de um script Python, carregue o arquivo para um bucket novo, para executar o 
		desafio. Utilize a biblioteca boto3.
		
**4**. Em outro script Python e a partir do arquivo que está dentro do S3, crie um dataframe 
com Pandas ou Polars e execute as seguintes manipulações:  
    
- **4.1** Uma cláusula que filtra dados usando ao menos dois operadores lógicos

- **4.2** Duas funções de agregação

- **4.3** Uma função condicional 

- **4.4** Uma função de conversão

- **4.5** Uma função de data

- **4.6** Uma função de string
    
**OBS**: Caso conseguir executar todas e retornar somente uma resposta, melhor será sua avaliação.
    
**5**. Após concluir essas etapas, salve o arquivo no formato csv e envie para o mesmo bucket criado para esse desafio. 
    Utilize boto3.
    
**6**. Armazene no Git um arquivo MD explicando seu conjunto de dados, bem como sua(s) consultas e o resultado da execução de suas consultas. Lembre-se:
    - Armazene o(s) arquivo(s) CSV.
    - Armazene o(s) arquivo(s) PY.
    - Armazene as evidências de execução com imagens JPEG ou PNG.

# Dataset 'cebas.csv'  
**CEBAS - Certificação de Entidades Beneficentes de Assistência Social** 

Neste conjunto de dados temos as seguintes variáveis:

**codigo_ibge**: código ibge do município.

**anome_s**: ano e mês de referência.

**cebas_cnpj_entidade_s**: Número de identificação do Cadastro Nacional de Pessoa Jurídica (CNPJ).

**cebas_razao_social_entidade_s**: Nome da Entidade constante no CNPJ.

**cebas_status_certificacao_s**: Status da Certificação, podendo ser válida (possui requerimento de 
renovação protocolado tempestivamente, aguardando decisão de mérito) ou vigente 
(CEBAS deferido com data da validade da Certificação constante na portaria de deferimento publicada 
no Diário Oficial da União).

**cebas_cod_status_certificacao_i**: Código do status da certificação, 1 - Válida, 2 - Vigente.

**cebas_dt_inicio_certificacao_s**: Data de início da certificação.

**cebas_dt_fim_certificacao_s**: Data fim da certificação.

**cebas_dt_extracao_dados_s**: Data da extração dos dados.

**cebas_qtd_certif_status_valida_i**: Quantidade de Entidades com status de Certificação válida.

**cebas_qtd_certif_status_vigente_i**: Quantidade de Entidades com status de Certificação vigente.



# Criação do Bucket  
Para a criação do bucket foi usado o script a seguir, criado a partir da referência da [documentação do boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/s3-examples.html) da própria AWS.

```python 
import boto3
from botocore.exceptions import ClientError, NoCredentialsError

# Configurações de credenciais
aws_access_key_id = sua_chave
aws_secret_access_key = sua_chave_secreta
session_token = seu_token

#Configurações adicionais
region_name = 'us-east-1'
bucket_name = 'desafio-sprint05-welder'

#Informações do arquivo
file_path = 'cebas.csv'
object_name = 'cebas-dataset.csv'

def criar_bucket(aws_access_key_id, aws_secret_access_key, session_token, region_name, bucket_name):
        try:
            #Criando client s3
            s3_client = boto3.client('s3', 
                        aws_access_key_id = aws_access_key_id,
                        aws_secret_access_key = aws_secret_access_key,
                        aws_session_token = session_token,
                        region_name = region_name )
                        
            #Criando o Bucket
            if region_name == 'us-east-1':
                response = s3_client.create_bucket(Bucket = bucket_name)
            
            else:
                response = s3_client.create_bucket(Bucket = bucket_name, CreateBucketConfiguration = {'LocationConstraint': region_name} )
                
            print(f"Bucket '{bucket_name}' criado com sucesso.")
            return response 
            
        except ClientError as cError:
            print(f"Erro ao criar bucket: {cError}")
            return None
```  
O script acima contém as credenciais de acesso à AWS para que seja feito de forma mais didática, porém é entendido como uma boa prática não colocar tais informações dentro do script. Uma outra maneira de configurar as credenciais é através do **aws configure** via terminal. Após seguir as solicitações necessárias, serão criados os arquivos credentials e config na pasta padrão da AWS (**.aws**) que servirão de referência para o boto3 fazer a autenticação.  

Dentro do mesmo script python também existe o código a seguir:  
```python
def enviar_arquivo(aws_access_key_id, aws_secret_access_key, session_token, bucket_name, file_path, object_name):
    
    s3 = boto3.client('s3', 
                        aws_access_key_id = aws_access_key_id,
                        aws_secret_access_key = aws_secret_access_key,
                        aws_session_token = session_token)
                        
    try:
        s3.upload_file(file_path, bucket_name, object_name)
        print(f"o Upload do arquivo '{object_name}' no Bucket '{bucket_name}' foi realizado com sucesso.")
    
    #Possíveis erros:
    except FileNotFoundError:
        print(f"Erro: O arquivo '{object_name}'não foi encontrado.")
    
    except NoCredentialsError:
        print('Erro: As credenciais da AWS estão inválidas ou não foram encontradas.')

    except Exception as exc:
        print(f"Erro Inesperado: {exc}")
        
response = criar_bucket(aws_access_key_id, aws_secret_access_key, session_token, region_name, bucket_name)
    
if response:
    print("Informações sobre a criação do bucket:", response)
        

enviar_arquivo(aws_access_key_id, aws_secret_access_key, session_token, bucket_name, file_path, object_name)
```

O código é utilizado para o arquivo descrito em **file_path** para o bucket especificado em **bucket_name**. O script está configurado para que o arquivo suba para o bucket com o nome especificado em **object_name**.  

Após a execução do código contendo as duas funções descritas acima, foi obtido o resultado:  
![criação do bucket + envio](../Evidencias/cria_envia.png)  

Pode-se verificar se, de fato, o script criou o bucket e enviou o arquivo para a AWS e esse passo está ilustrado nas duas figuras a seguir.  
### Criação do bucket do desafio
![buckets](../Evidencias/buckets_exercicio_desafio.png)  
#
### Objeto enviado para o bucket
![objeto no bucket](../Evidencias/objeto_bucket.png)  

O próximo passo foi fazer o download do arquivo **.csv** que agora está no bucket para que sejam feitas as manipulações localmente. O arquivo foi puxado do bucket com o nome **dataset-baixado**.  

Para fazer o download do arquivo foi usado o script a seguir:  

```python 
import boto3
from botocore.exceptions import ClientError, NoCredentialsError

aws_access_key_id = sua_chave
aws_secret_access_key = sua_chave_secreta
session_token = seu_token

bucket_name = 'desafio-sprint05-welder' #nome do bucket já existente
object_name = 'cebas-dataset.csv' #nome do arquivo no bucket 
download_path = 'dataset-baixado.csv' #salva o arquivo baixado na mesma pasta que está o script

def baixar_arquivo_do_bucket(aws_access_key_id, aws_secret_access_key, session_token, bucket_name, object_name, download_path):
    try:
        #criando o client no s3
        s3_client = boto3.client('s3', 
                        aws_access_key_id = aws_access_key_id,
                        aws_secret_access_key = aws_secret_access_key,
                        aws_session_token = session_token)
                        
        #baixando o arquivo do bucket 
        s3_client.download_file(bucket_name, object_name, download_path)
        print(f"O arquivo '{object_name}' foi baixado com sucesso.")      
    
    except FileNotFoundError:
        print("O caminho especificado para o download não foi encontrado.")

    except NoCredentialsError:
        print("Erro: As credenciais da AWS estão inválidas ou não foram encontradas.")
        
    except ClientError as cError:
        print(f"Erro ao fazer o download do arquivo: {cError}")

#Executando a função para download do arquivo
baixar_arquivo_do_bucket(aws_access_key_id, aws_secret_access_key, session_token,
    bucket_name, object_name, download_path)
``` 

O resultado obtido está ilustrado na figura a seguir.  
![download do dataset ](../Evidencias/download_objeto.png)  

## Manipulações dos dados 
Para responder à pergunta **"Quais entidades possuem a palavra "Hospital", "Hospitalidade" ou alguma variação desse tipo no nome, têm status de certificação vigente, e começaram sua certificação em 2021, retornando o total de entidades em cada status (válida e/ou vigente), a duração da certificação (em dias) e o nome da entidade com a primeira letra maiúscula e o resto minúscula?"** foi utilizado o script python com o código mostrado a seguir.  

```python 
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

#4.4 Uma função de conversão
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
```

O script é responsável por retornar um arquivo .csv com o dataset limpo (após retirada dos valores NaN), outro arquivo .csv com o dataframe auxiliar utilizado após os filtros e, por último, um outro arquivo .csv com o resultado das funções de agregação aplicadas.  
Sua execução pode ser observada nas figuras a seguir.
![manipulações 1](../Evidencias/manipulacoes1.png)
![manipulações 2](../Evidencias/manipulacoes2.png)  
![manipulações 1](../Evidencias/manipulacoes3.png)  
![manipulações 1](../Evidencias/manipulacoes4.png)  

# Links
[📜**Certificados**](/Sprint5/Certificados/)  
[🕵️‍♂️**Evidências** ](/Sprint5/Evidencias/)  
[💪**Exercícios**](/Sprint5/Exercicios/)  
[🖳 **Desafio**](/Sprint5/Desafio/README.md)  







 


