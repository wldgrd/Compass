import boto3
from botocore.exceptions import ClientError, NoCredentialsError

# Configurações de credenciais
aws_access_key_id = 'chave'
aws_secret_access_key = 'chave_secreta'
session_token = 'token'

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