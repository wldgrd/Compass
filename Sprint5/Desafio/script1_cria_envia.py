import boto3
from botocore.exceptions import ClientError, NoCredentialsError

# Configurações de credenciais
aws_access_key_id = 'ASIAWPPO6JPYL4BVLIOX'
aws_secret_access_key = 'CvYqg6K25Or9olbH78OKJfWc2qI5E/K/esAaLeb1'
session_token = 'IQoJb3JpZ2luX2VjEAQaCXVzLWVhc3QtMSJHMEUCIQCC3S4BAlkACzGwMDAq5++IEweWuSfDoYF6klEuL5XuLwIgFZWZMX3ldg7zXEpVTQq3RoyVuFMXot/4xc/n9q6+vLwqqgMIzf//////////ARAAGgw0NDU1NjcwOTM3NDQiDIIhFVuL/dYPKcHLuCr+ArB1ZlfJQRUBNtTcFyGUZolqDakW5UEN4+sHMTKXGtPxzFuYd/lzRpdEbkkn8kgXsOK1h4xTm4Bzcjb8Awfz4Td1BAkYXBs1TdxD6x0YhXktXoE84ugKhov3uXZGP0C7cIhFKlRo9IgGav3W1xMU7ebbYIGZoIkjfrZIVIBCUfEqI72BCDeNGwdbri1uqjyz5xLHJRNiWLk5F4CEAAOeKUO5VSNysU2Rzj9flK9yntUt2g7swZhOyDjw4pd+SbmhE9lOT/frCO8njEFpRh4LRpeFAkKdoUdyHL8O99qkSbPk6kuDVujl+8b1C7JZsJSYzj6NLSpIU/wT0530Ii5bt9Y5+XVtP5B4rg03q4LIaj3HwUJ8AQbla6slBzjzuCAMBcbKR7Qm2i3EKI0gB2o3Hknfp2UQpyx9vdGuH3sLeaq4Nx0gRYWHcZE95g+fSs82BU81+DPi9PpbWb1TMIU50+2PVlo79UgFSNc9rbRvxG1iCuwZNKDv+amHoOZBpMkw3bOjuwY6pgFXFj7iZIPXr28BzdTAGkXcebNMXEnuLyKllCqz3Fiwo7/wLb2fosAjCsBMAzsG1pWGBlQp53QXARFnVqPT/RS4j0Dgb8zEj65Vzj4X+XcqHjhjf1dRXR7E3uvg0jK8SmNgTUxbLsQggqY+TFVtLG6rbx+FUiSD6wOz4sZQSqqTtug7Dxrlw0X4bsQcmhJV4locWlBfW5yCu9rNsELtJ8uuxdYTmXIi'

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
    s3_client = boto3.client('s3', 
                        aws_access_key_id = aws_access_key_id,
                        aws_secret_access_key = aws_secret_access_key,
                        aws_session_token = session_token)
                        
    try:
        s3.upload_file(file_path, bucket_name, object_name)
        print(f"o Upload do arquivo '{object_name}' no Bucket '{bucket_name}'")
    
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