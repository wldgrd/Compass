import sys
from pyspark.context import SparkContext
from pyspark.sql import SparkSession
from pyspark.conf import SparkConf
from awsglue.context import GlueContext
from awsglue.job import Job
from awsglue.dynamicframe import DynamicFrame
import pyspark.sql.functions as F
import pyspark.sql.types as T
from awsglue.utils import getResolvedOptions

args = getResolvedOptions(sys.argv, ['JOB_NAME', 'S3_INPUT_PATH', 'S3_TARGET_PATH'])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

source_file = args['S3_INPUT_PATH']
target_path = args['S3_TARGET_PATH']

# Definição dos tipos das colunas
schema = T.StructType([
    T.StructField("id", T.StringType(), True),
    T.StructField("tituloPincipal", T.StringType(), True),  
    T.StructField("tituloOriginal", T.StringType(), True),
    T.StructField("anoLancamento", T.IntegerType(), True),
    T.StructField("tempoMinutos", T.IntegerType(), True),  # Pode conter valores "\N"
    T.StructField("genero", T.StringType(), True),
    T.StructField("notaMedia", T.DoubleType(), True),
    T.StructField("numeroVotos", T.IntegerType(), True),
    T.StructField("generoArtista", T.StringType(), True),
    T.StructField("personagem", T.StringType(), True),
    T.StructField("nomeArtista", T.StringType(), True),
    T.StructField("anoNascimento", T.StringType(), True),  # Pode conter valores "\N"
    T.StructField("anoFalecimento", T.StringType(), True),  # Pode conter valores "\N"
    T.StructField("profissao", T.StringType(), True),
    T.StructField("titulosMaisConhecidos", T.StringType(), True)
])

# Lendo o arquivo CSV
df = spark.read.csv(source_file, schema=schema, sep='|', header=True)

# Corrigindo o nome da coluna
df = df.withColumnRenamed("tituloPincipal", "tituloPrincipal")

# Exibindo as 10 primeiras linhas no log
df.show(10)

# Escrevendo no formato Parquet
#df.write.mode("overwrite").parquet(target_path)
df.coalesce(1).write.mode("overwrite").parquet(target_path)

# Finalizando o job
job.commit()
