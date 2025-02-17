import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from awsglue.context import GlueContext
from awsglue.job import Job
from pyspark.context import SparkContext
from pyspark.sql.functions import explode, col
from awsglue.dynamicframe import DynamicFrame

args = getResolvedOptions(sys.argv, ['JOB_NAME', 'S3_INPUT_PATH', 'S3_TARGET_PATH'])
input_path = args['S3_INPUT_PATH']
target_path = args['S3_TARGET_PATH']

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

dyf = glueContext.create_dynamic_frame.from_options(
    connection_type="s3",
    connection_options={"paths": [input_path]},
    format="parquet"
)

#Converter para DataFrame Spark
df = dyf.toDF()

#Criar Tabela Fato (fato_filmes)
fato_filmes = df.select(
    "id", "imdb_id", "budget", "popularity", "release_date", "runtime", "vote_average", "vote_count"
)

#Criar Dimensão Gêneros (dim_generos)
dim_generos = df.withColumn("genre", explode(col("genres")))
dim_generos = dim_generos.selectExpr("id as movie_id", "genre.id as genre_id", "genre.name as genre_name")

#Criar Dimensão Elenco (dim_elenco)
dim_elenco = df.withColumn("cast_member", explode(col("cast")))
dim_elenco = dim_elenco.selectExpr(
    "id as movie_id", "cast_member.id as cast_id", "cast_member.name as name", 
    "cast_member.character as character", "cast_member.birthday as birthday", 
    "cast_member.deathday as deathday", "cast_member.gender as gender", 
    "cast_member.popularity as popularity"
)

#Criar Dimensão Empresas (dim_empresas)
dim_empresas = df.withColumn("company", explode(col("production_companies")))
dim_empresas = dim_empresas.selectExpr("id as movie_id", "company.id as company_id", "company.name as company_name", "company.origin_country as company_country")

#Criar Dimensão Países (dim_países)
dim_paises = df.withColumn("country", explode(col("production_countries")))
dim_paises = dim_paises.selectExpr("id as movie_id", "country.iso_3166_1 as iso_3166_1", "country.name as country_name")

#Criar Dimensão Idiomas (dim_idiomas)
dim_idiomas = df.withColumn("language", explode(col("spoken_languages")))
dim_idiomas = dim_idiomas.selectExpr("id as movie_id", "language.iso_639_1 as iso_639_1", "language.english_name as english_name", "language.name as name")

#Salvar tabelas no S3 para uso no Glue Data Catalog
fato_filmes.write.mode("overwrite").parquet(f"{target_path}/fato_filmes")
dim_generos.write.mode("overwrite").parquet(f"{target_path}/dim_generos")
dim_elenco.write.mode("overwrite").parquet(f"{target_path}/dim_elenco")
dim_empresas.write.mode("overwrite").parquet(f"{target_path}/dim_empresas")
dim_paises.write.mode("overwrite").parquet(f"{target_path}/dim_paises")
dim_idiomas.write.mode("overwrite").parquet(f"{target_path}/dim_idiomas")

job.commit()
