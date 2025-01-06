# Objetivo  
O objetivo é praticar a combinação de conhecimentos vistos no programa e fazer um mix de tudo que já foi dito.  

# Instruções Gerais  
ENTREGA 1

Ingestão Batch:
	
a ingestão dos arquivos CSV em Bucket Amazon S3 RAW Zone. Nesta etapa do desafio deve ser construído um 
código Python que será executado dentro de um container Docker para carregar os dados locais dos arquivos 
disponibilizados para a nuvem. Nesse caso utilizaremos, principalmente, a lib boto3 como parte do processo
de ingestão via batch para geração de arquivo CSV.  
	
1. Implementar código Python:
	- ler os 2 arquivos (movies.csv e series.csv) no formato CSV inteiros, ou seja, sem filtrar os dados.
	- utilizar a lib boto3 para carregar os dados para a AWS 
	- acessar a AWS e gravar no S3, no Bucket definido como RAW Zone
	
	- No momento da gravação dos dados deve-se considerar o padrão:
		<nome_do_bucket>\<camada_de_armazenamento>\<origem_do_dado>\<formato_do_dado>\<especificação_do_dado>\<data_de_processamento_separada_por_ano\mes\dia>\<arquivo>
		
		Por exemplo:
		
		S3:\\data-lake-do-fulano\Raw\Local\CSV\Movies\2022\05\02\movies.csv
		
		S3:\\data-lake-do-fulano\Raw\Local\CSV\Series\2022\05\02\series.csv 
		
2. Criar container Docker com um volume para armazenar os arquivos CSV e executar processo Python implementado.

3. Executar localmente o container docker para realizar a carga dos dados ao S3.






# Links
[📜**Certificados**](/Sprint6/Certificados/)  
[🕵️‍♂️**Evidências** ](/Sprint6/Evidencias/)  
[💪**Exercícios**](/Sprint6/Exercicios/)  
[🖳 **Desafio**](/Sprint6/Desafio/README.md)  