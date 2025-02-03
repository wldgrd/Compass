import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from awsglue.context import GlueContext
from awsglue.job import Job
from pyspark.context import SparkContext

# Obter argumentos do Glue
args = getResolvedOptions(sys.argv, ['JOB_NAME', 'S3_INPUT_PATH', 'S3_TARGET_PATH'])
input_path = args['S3_INPUT_PATH']
target_path = args['S3_TARGET_PATH']

# Criar contexto do Glue
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# Ler todos os arquivos JSON da pasta
df = spark.read.option("multiline", "true").json(input_path)

# Salvar como Parquet
df.write.mode("overwrite").parquet(target_path)

print(f"Arquivos Parquet salvos em: {target_path}")

job.commit()
