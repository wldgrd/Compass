import boto3
from botocore.exceptions import ClientError, NoCredentialsError

# Configurações de credenciais
aws_access_key_id = 'ASIAWPPO6JPYDI4PWN4J'
aws_secret_access_key = '8LGL2c6smjKi14nafGkSnWBbaUTD++oA31FUPewV'
session_token = 'IQoJb3JpZ2luX2VjEA8aCXVzLWVhc3QtMSJGMEQCICZ4ZJEDNIcgyxuevdK+SCsNdzf35MqxdHLPvXPw6e4uAiAf1UwwqIWXk6cPit0bVcGLlLr/xy+EDaX4cUxWVO+HQyqqAwjY//////////8BEAAaDDQ0NTU2NzA5Mzc0NCIM8oEgKde1d+ysuexxKv4CnFswsgNSVTrFEjIWBgnlZGIJJuj4XkDpkwmjZ94SRLgij/DMAqDmCmJD6MejE1RoYEks0B6X7BwZbmUnO3/eqoGd8y185hj0pxE7UFa3vxrnn1JKQ9EyuBaJnBUYqndWaojF6sW7SxmtJKcoP8iDcPiFFY82YfwWByOAgBzFRJhAuRg8HDawIemPdt9w/DZmVly3XbrbheaZScAO7TdWESRWlLkbyEYdD8tvxGelGsA6m/HI/j7z96Tlb6S9k9a6Ht3S6SQRect5YPEJdsNv4pmOl1mbFYjQBmBnDI9zFZiC7aCzpVMUW35ONtYPTH1jLSL0EGjcRNNdvMSMf7sJhk4FXLNa3kyxPW4dZhILk+Np85UHmXYO2HAmvT6q5/OeXvKw1Sz42HK5ccLoA/YpS+VJUK4GJkK4wosU7+K+msOVTVQcY1imSlZp+bYSXE9CAgDmhSn05W+8/bdTcc0JDdT8jR795QfmRr8y6HvaqJOg0jrotIzuhfAsDhmJ7TD77aW7BjqnASUtoZJbN3n7Vm/ibed3yDJrb2yCa7MJg7yYokyJIn++bIqYuxHGInTcUniOfKtjUWE1BiadfwUE0zrVQmOuhBMfXJ5fbiphOpzduUnYXw6p0WXobF7JeLjYWM4gjx3Y+9tBFXpIwV2gzyH5yCECz3j7lx4fXjv5djVXSDUrbWjFbcskDEPc/qP1sjWG5FTSy2tGrrQBnjxzIMFdBrS/RrFK8/ODC9EJ'

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