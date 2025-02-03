# Resumo
Nessa sprint, usamos o Pyspark juntamente com o Glue para o processamento dos dados e criação da camada **trusted** do datalake criado usando o S3.
  

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


# Exercícios  
1. **Execução do exercício "Geração de massa de dados".**  
![massa](/Sprint8/Exercicios/massa1.png)  
![massa](/Sprint8/Exercicios/massa2.png)  
![massa](/Sprint8/Exercicios/massa3.png)   
  

2. **Execução do exercício sobre Apache Spark. (Executado no Google Colab)**  
![spark](/Sprint8/Exercicios/spark1.png)
![spark](/Sprint8/Exercicios/spark2.png)
![spark](/Sprint8/Exercicios/spark3.png)
![spark](/Sprint8/Exercicios/spark4.png)
![spark](/Sprint8/Exercicios/spark5.png)
![spark](/Sprint8/Exercicios/spark6.png)
![spark](/Sprint8/Exercicios/spark7.png)
![spark](/Sprint8/Exercicios/spark8.png)
![spark](/Sprint8/Exercicios/spark9.png)
![spark](/Sprint8/Exercicios/spark10.png)
![spark](/Sprint8/Exercicios/spark11.png)
![spark](/Sprint8/Exercicios/spark12.png)




# Links
[📜**Certificados**](/Sprint8/Certificados/)  
[🕵️‍♂️**Evidências** ](/Sprint8/Evidencias/)  
[💪**Exercícios**](/Sprint8/Exercicios/)  
[🖳 **Desafio**](/Sprint8/Desafio/README.md)  