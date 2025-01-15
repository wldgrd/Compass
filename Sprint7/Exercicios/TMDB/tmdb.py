import requests
import pandas as pd
from IPython.display import display 

api_key = "44a51a00d9f1c02bb28e87d10f642984"

url = f"https://api.themoviedb.org/3/movie/top_rated?api_key={api_key}&language=pt-BR"

response = requests.get(url)
data = response.json()

filmes = []

for movie in data['results']:
	df = {'Titulo': movie['title'],
	'Data de lançamento': movie['release_date'],
	'Visão geral': movie['overview'],
	'Votos': movie['vote_count'],
	'Média dos votos': movie['vote_average']}
	
	filmes.append(df)
	
df = pd.DataFrame(filmes)
display(df)