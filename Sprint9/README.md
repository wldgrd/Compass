# Resumo
Nessa sprint, usamos o Pyspark juntamente com o Glue para o processamento dos dados e criação da camada **refined** do datalake criado usando o S3 e, por fim, o Athena para as consultas SQL.
  

## Amazon S3 (Simple Storage Service)
O Amazon Simple Storage Service (Amazon S3) é um serviço de armazenamento de objetos que oferece escalabilidade, disponibilidade de dados, segurança e performance líderes do setor. Clientes de todos os portes e setores podem armazenar e proteger qualquer quantidade de dados de praticamente qualquer caso de uso, como data lakes, aplicações nativas da nuvem e aplicações móveis. Com classes de armazenamento econômicas e recursos de gerenciamento fáceis de usar, você pode otimizar custos, organizar dados e configurar controles de acesso ajustados para atender a requisitos específicos de negócios, organizacionais e de conformidade.

![Esquemático S3](../img/s3.png)
Fonte: https://aws.amazon.com/pt/s3/ (acesso em 23/12/2024)  

#  
## AWS Glue  
O AWS Glue é um serviço de integração de dados com tecnologia sem servidor que facilita aos usuários de análise a descoberta, preparação, transferência e integração de dados de várias fontes. Você pode usá-lo para análise, machine learning e desenvolvimento de aplicações. Também inclui outras ferramentas de produtividade e operações de dados para criação, execução de trabalhos e implementação de fluxos de trabalho de negócios.

Com o AWS Glue, você pode detectar e se conectar a mais de 70 fontes de dados diversas e gerenciar seus dados em um catálogo de dados centralizado. Você pode criar, executar e monitorar visualmente pipelines de extração, transformação e carregamento (ETL) para carregar dados em seus data lakes. Além disso, é possível pesquisar e consultar imediatamente os dados catalogados usando o Amazon Athena, o Amazon EMR e o Amazon Redshift Spectrum.

O AWS Glue consolida os principais recursos de integração de dados em um único serviço. Isso inclui descoberta de dados, ETL moderno, limpeza, transformação e catalogação centralizada. Também conta com tecnologia sem servidor, o que significa que não há infraestrutura para gerenciar. Com suporte flexível para todas as workloads, como ETL, ELT e transmissão em um único serviço, o AWS Glue oferece suporte a usuários em várias workloads e tipos de usuários.

Além disso, o AWS Glue facilita a integração de dados em sua arquitetura. Ele se integra aos serviços de análise da AWS e a data lakes do Amazon S3. O AWS Glue tem interfaces de integração e ferramentas de criação de trabalhos que são descomplicadas para todos os usuários, de desenvolvedores a usuários corporativos, com soluções personalizadas para conjuntos variados de habilidades técnicas.  
**Fonte:** Documentação oficial AWS  
#

## Apache Spark  
**O que é Apache Spark ?**  
O Apache Spark é um mecanismo multilinguagem para executar engenharia de dados, ciência de dados e aprendizado de máquina em máquinas de nó único ou clusters.  
<br>
**Principais características:**  
1. **Dados em lote/streaming**  
    Unifique o processamento dos seus dados em lotes e streaming em tempo real, usando sua linguagem preferida: Python, SQL, Scala, Java ou R.  

2. **Análise SQL:**  
Execute consultas ANSI SQL rápidas e distribuídas para dashboarding e relatórios ad-hoc. Executa mais rápido do que a maioria dos data warehouses.  

3. **Ciência de dados em escala:**  
Realizar Análise Exploratória de Dados (EDA) em dados em escala de petabytes sem precisar recorrer à redução de amostragem.  

4. **Aprendizado de máquina:**  
Treine algoritmos de aprendizado de máquina em um laptop e use o mesmo código para escalar para clusters tolerantes a falhas de milhares de máquinas.  

#
## Athena  
O Amazon Athena é um serviço de consultas interativas da Amazon Web Services (AWS) que facilita a análise de dados diretamente no Amazon Simple Storage Service (S3) usando linguagem SQL padrão. Com apenas algumas ações no AWS Management Console, é possível direcionar o Athena para os dados armazenados no S3 e começar a usar o SQL para executar consultas.

**Principais características**  
**Sem servidor:**  
O Athena não exige configuração ou gerenciamento de servidores, o que significa que você se concentra apenas na análise dos dados.  
**Fácil de usar:**  
A interface do Athena é intuitiva e permite que você execute consultas SQL de forma rápida e fácil.  

**Escalável:**  
O Athena escala automaticamente para lidar com grandes volumes de dados e consultas complexas.  

**Integrado com o S3:**  
O Athena se integra perfeitamente com o S3, o serviço de armazenamento de objetos da AWS, permitindo que você consulte dados armazenados em diferentes formatos, como CSV, JSON, Parquet e ORC.  

**Econômico:**  
Você paga apenas pelas consultas que executa, o que torna o Athena uma solução econômica para análise de dados.
Como funciona
Você aponta o Athena para os dados armazenados no S3.
O Athena usa o Presto, um mecanismo de consulta distribuído de código aberto, para executar consultas SQL nos dados.
Os resultados da consulta são exibidos no console do Athena ou podem ser enviados para outros serviços da AWS, como o Amazon QuickSight, para visualização.  

**Casos de uso**  

**Análise de logs:**  
O Athena pode ser usado para analisar logs de aplicativos, servidores e outros dispositivos para identificar problemas, tendências e padrões.  

**Business intelligence:**  
O Athena pode ser usado para gerar relatórios e dashboards para análise de dados de negócios.
Ciência de dados: o Athena pode ser usado para explorar e analisar grandes conjuntos de dados para identificar insights e construir modelos de machine learning.  



# Links
[📜**Certificados**](/Sprint9/Certificados/)  
[🕵️‍♂️**Evidências** ](/Sprint9/Evidencias/)  
[💪**Exercícios**](/Sprint9/Exercicios/)  
[🖳 **Desafio**](/Sprint9/Desafio/README.md)  