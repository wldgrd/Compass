import boto3
from botocore.exceptions import ClientError, NoCredentialsError

aws_access_key_id = 'ASIAWPPO6JPYNW2MQJTN'
aws_secret_access_key = 'D+8CS8WowysgluN/qTXP/1q+hZFrNtmwTlGyS/da'
session_token = 'IQoJb3JpZ2luX2VjEOb//////////wEaCXVzLWVhc3QtMSJHMEUCIQClupbUq

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