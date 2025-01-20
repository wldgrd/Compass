import os
import boto3
import requests
import json
from datetime import datetime
from botocore.exceptions import ClientError

#enviando arquivos para o bucket
def enviar_arquivo(bucket_name, file_path, object_name, s3_client):
    try:
        s3_client.upload_file(file_path, bucket_name, object_name)
        print(f"Upload do arquivo '{object_name}' no Bucket '{bucket_name}' foi realizado com sucesso.")
    except FileNotFoundError:
        print(f"Erro: O arquivo '{file_path}' não foi encontrado.")
    except ClientError as e:
        print(f"Erro ao enviar o arquivo para o S3: {e}")
    except Exception as exc:
        print(f"Erro inesperado: {exc}")

#definindo o caminho conforme o padrão solicitado
def build_s3_path(file, bucket_name='desafio-final-pb-welder'):
    date = datetime.now()
    year = date.year
    month = date.month
    day = date.day
    path = f"Raw/TMDB/JSON/{year}/{month:02d}/{day:02d}/{file}"
    return path

#dividir o arquivo JSON baixado em partes com 100 registros
def dividir_json(data, max_registros=100):
    for i in range(0, len(data), max_registros):
        yield data[i:i + max_registros]

#buscar dados na API do TMDB
def fetch_tmdb_data(api_key, media_type='movie', page=1, genres=[80, 10752]):
    all_results = []  # Lista para armazenar todos os resultados combinados
    
    for genre_id in genres:  # Iterar sobre os gêneros especificados
        url = f'https://api.themoviedb.org/3/discover/{media_type}?api_key={api_key}&page={page}&with_genres={genre_id}'
        response = requests.get(url)
        
        if response.status_code == 200:
            all_results.extend(response.json().get('results', []))  # Adicionar os resultados à lista
        else:
            print(f"Erro ao buscar dados do TMDB para o gênero {genre_id}: {response.status_code}")
    
    return all_results

#função principal lambda
def lambda_handler(event, context):
    #variáveis de ambiente
    api_key = os.environ['TMDB_API_KEY']
    bucket_name = 'desafio-final-pb-welder'
    
    #inicializando client S3
    s3_client = boto3.client('s3')
    
    #tipos de mídia (filmes e séries)
    media_types = ['movie', 'tv']  # 'movie' para filmes e 'tv' para séries
    
    #gêneros de interesse (crime = 80, guerra = 10752)
    genres = [80, 10752]
    
    for media_type in media_types:
        all_data = []
        page = 1
                
        while True:
            data = fetch_tmdb_data(api_key, media_type, page, genres)
            if not data:  #caso não haver mais dados, parar para evitar loop infinito.
                break
            all_data.extend(data)
            page += 1
        
        #dividindo o arquivo em subarquivos
        for idx, data_chunk in enumerate(dividir_json(all_data, max_registros=100)):
            #criando arquivo JSON temporário em /tmp
            file_name = f"/tmp/{media_type}_dados_{datetime.now().strftime('%Y%m%d%H%M%S')}_{idx + 1}.json"
            with open(file_name, 'w', encoding='utf-8') as f:
                json.dump(data_chunk, f, ensure_ascii=False, indent=4)
            
            s3_path = build_s3_path(file_name.split('/')[-1], bucket_name)
            
            enviar_arquivo(bucket_name, file_name, s3_path, s3_client)

            #removendo o arquivo local após envio para o S3
            os.remove(file_name)
        
    return {
        'statusCode': 200,
        'body': json.dumps('Arquivos processados e enviados para o S3 com sucesso.')
    }
