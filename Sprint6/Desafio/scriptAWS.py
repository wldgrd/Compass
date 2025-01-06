#-------Bibliotecas-------#

import boto3
import pandas as pd
from datetime import datetime 
from botocore.exceptions import ClientError, NoCredentialsError

#------------------------------------------------------------------------------------------------#

#Função para enviar arquivos para um bucket já existente - criada na Sprint5
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

#Construindo o caminho conforme padrão solicitado

def buildS3Path(file, source, bucketName = 'desafio-final-pb-welder'):
    date = datetime.now()
    year = date.year
    month = date.month
    day = date.day 

    #Caminho
    path = f"Raw/Local/CSV/{source}/{year}/{month:02d}/{day:02d}/{file}"

    return path 

def main():
    
    #Bucket principal
    bucketName = 'desafio-final-pb-welder'
    
    #Dicionário dos arquivos e suas origens
    arquivos = [
        {"file": "movies.csv", "source": "Movies"},
        {"file": "series.csv", "source": "Series"}
    ]

    for arquivo in arquivos:
        file = arquivo["file"]
        source = arquivo["source"]

        #Criando o dataframe 
        df = pd.read_csv(file, sep = '|')

        #Criando o caminho no bucket
        s3Path = buildS3Path(file, source, bucketName)

        #Subindo os arquivos para o bucket
        enviar_arquivo(aws_access_key_id, aws_secret_access_key, aws_session_token, bucketName, file, s3Path )


aws_access_key_id = input('Insira sua chave de acesso AWS: ')
aws_secret_access_key = input('Insira sua chave de acesso secreta AWS: ')
aws_session_token = input('Insira o token da sua sessão AWS: ')

main()

