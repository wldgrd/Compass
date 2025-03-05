import sys
from awsglue.utils import getResolvedOptions
from awsglue.context import GlueContext
from awsglue.job import Job
from pyspark.context import SparkContext
from pyspark.sql.functions import explode, col, lit, year, month, dayofmonth, row_number
from awsglue.dynamicframe import DynamicFrame
from pyspark.sql import Window

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
df = dyf.toDF().dropDuplicates()

# Criar Dimensão Tempo
dim_tempo = df.select(col("release_date").alias("data")) \
    .withColumn("ano", year(col("data"))) \
    .withColumn("mes", month(col("data"))) \
    .withColumn("dia", dayofmonth(col("data"))) \
    .dropDuplicates() \
    .withColumn("id_tempo", row_number().over(Window.orderBy(col("data"))))

# Criar Dimensão Idiomas
dim_idiomas = df.withColumn("language", explode(col("spoken_languages"))) \
    .select(
        col("language.iso_639_1").alias("iso_639_1"),
        col("language.english_name").alias("english_name")
    ).dropDuplicates() \
    .withColumn("id_idioma", row_number().over(Window.orderBy(lit(1))))

# Criar Dimensão Países
dim_paises = df.withColumn("country", explode(col("production_countries"))) \
    .select(
        col("country.iso_3166_1").alias("iso_3166_1"),
        col("country.name").alias("country_name")
    ).dropDuplicates() \
    .withColumn("id_pais", row_number().over(Window.orderBy(lit(1))))

# Criar Dimensão Empresas
dim_empresas = df.withColumn("company", explode(col("production_companies"))) \
    .select(
        col("company.name").alias("company_name")
    ).dropDuplicates() \
    .withColumn("id_empresa", row_number().over(Window.orderBy(lit(1))))

# Criar Dimensão Gêneros
dim_generos = df.withColumn("genre", explode(col("genres"))) \
    .select(
        col("genre.name").alias("genre_name")
    ).dropDuplicates() \
    .withColumn("id_genero", row_number().over(Window.orderBy(lit(1))))

# Criar Tabela Fato
fato_filmes = df.select(
    col("id").alias("movie_id"),
    col("budget"),
    col("popularity"),
    col("runtime"),
    col("vote_average"),
    col("vote_count"),
    col("release_date").alias("data"),
    col("spoken_languages").getItem(0).getField("iso_639_1").alias("idioma_iso")
).dropDuplicates() \
.withColumn("id_filme", row_number().over(Window.orderBy(lit(1))))

fato_filmes = fato_filmes.join(dim_tempo, fato_filmes.data == dim_tempo.data, "left").drop(dim_tempo.data).drop(fato_filmes.data)
fato_filmes = fato_filmes.join(dim_idiomas, fato_filmes.idioma_iso == dim_idiomas.iso_639_1, "left") \
    .drop(dim_idiomas.iso_639_1).drop(fato_filmes.idioma_iso) \
    .withColumnRenamed("id_idioma", "id_idioma")

# Reorganizar colunas na tabela fato_filmes
fato_filmes = fato_filmes.select(
    "id_filme", "id_tempo", "id_idioma", "movie_id", "budget", "popularity", "runtime", "vote_average", "vote_count"
)

# Criar Tabelas Intermediárias corretamente antes do JOIN
fato_filmes_has_dim_paises = df.withColumn("country", explode(col("production_countries"))).dropna() \
    .select(col("id").alias("movie_id"), col("country.iso_3166_1").alias("iso_3166_1")) \
    .join(fato_filmes, "movie_id", "left") \
    .join(dim_paises, "iso_3166_1", "left") \
    .select(col("id_filme").alias("fato_filmes_id_filme"), col("id_pais").alias("dim_paises_id_pais"))

fato_filmes_has_dim_generos = df.withColumn("genre", explode(col("genres"))).dropna() \
    .select(col("id").alias("movie_id"), col("genre.name").alias("genre_name")) \
    .join(fato_filmes, "movie_id", "left") \
    .join(dim_generos, "genre_name", "left") \
    .select(col("id_filme").alias("fato_filmes_id_filme"), col("id_genero").alias("dim_generos_id_genero"))

fato_filmes_has_dim_empresas = df.withColumn("company", explode(col("production_companies"))).dropna() \
    .select(col("id").alias("movie_id"), col("company.name").alias("company_name")) \
    .join(fato_filmes, "movie_id", "left") \
    .join(dim_empresas, "company_name", "left") \
    .select(col("id_filme").alias("fato_filmes_id_filme"), col("id_empresa").alias("dim_empresas_id_empresa"))

# Salvar tabelas
fato_filmes.write.mode("overwrite").parquet(f"{target_path}/fato_filmes")
dim_tempo.write.mode("overwrite").parquet(f"{target_path}/dim_tempo")
dim_idiomas.write.mode("overwrite").parquet(f"{target_path}/dim_idiomas")
dim_paises.write.mode("overwrite").parquet(f"{target_path}/dim_paises")
dim_empresas.write.mode("overwrite").parquet(f"{target_path}/dim_empresas")
dim_generos.write.mode("overwrite").parquet(f"{target_path}/dim_generos")
fato_filmes_has_dim_paises.write.mode("overwrite").parquet(f"{target_path}/fato_filmes_has_dim_paises")
fato_filmes_has_dim_generos.write.mode("overwrite").parquet(f"{target_path}/fato_filmes_has_dim_generos")
fato_filmes_has_dim_empresas.write.mode("overwrite").parquet(f"{target_path}/fato_filmes_has_dim_empresas")

job.commit()