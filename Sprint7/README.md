# Resumo
Nessa sprint, aprendemos sobre Spark, Hadoop , AWS Glue e voltamos a usar o Lambda juntamente com o S3 para dar sequência na criação do data lake.
  

## Amazon S3 (Simple Storage Service)
O Amazon Simple Storage Service (Amazon S3) é um serviço de armazenamento de objetos que oferece escalabilidade, disponibilidade de dados, segurança e performance líderes do setor. Clientes de todos os portes e setores podem armazenar e proteger qualquer quantidade de dados de praticamente qualquer caso de uso, como data lakes, aplicações nativas da nuvem e aplicações móveis. Com classes de armazenamento econômicas e recursos de gerenciamento fáceis de usar, você pode otimizar custos, organizar dados e configurar controles de acesso ajustados para atender a requisitos específicos de negócios, organizacionais e de conformidade.

![Esquemático S3](../img/s3.png)
Fonte: https://aws.amazon.com/pt/s3/ (acesso em 23/12/2024)  

 
# 

## AWS Lambda  
Lambda é um serviço de computação ideal para cenários de aplicativos que precisam aumentar rapidamente e diminuir para zero quando não há demanda. Por exemplo, você pode usar Lambda para:

Processamento de arquivos: use o Amazon Simple Storage Service (Amazon S3) para acionar o processamento de dados do Lambda em tempo real após um upload.

Aplicativos Web: combine o Lambda com outros serviços da AWS para criar aplicativos Web poderosos que aumentam e diminuem automaticamente e são executados em uma configuração de alta disponibilidade em vários data centers.

Backends de IoT: crie backends sem servidor usando Lambda para lidar com solicitações de API da Web, dispositivos móveis, IoT e de terceiros.

Backends móveis: crie backends usando Lambda e Amazon API Gateway para autenticar e processar solicitações de API. Use o AWS Amplify para integrar facilmente com seus frontends iOS, Android, Web e React Native.

Ao usar o Lambda, você é responsável apenas pelo seu código. O Lambda gerencia a frota de computação que oferece um equilíbrio de memória, CPU, rede e outros recursos para executar seu código. Como o Lambda gerencia esses recursos, você não pode efetuar login em instâncias de computação ou personalizar o sistema operacional em tempos de execução fornecidos. O Lambda executa atividades operacionais e administrativas em seu nome, incluindo gerenciamento de capacidade, monitoramento e registro em log de suas funções do Lambda.  

### Principais características 

Os seguintes recursos principais ajudam você a desenvolver aplicativos Lambda que são escaláveis, seguros e facilmente extensíveis:

**Variáveis ​​de ambiente**  
Use variáveis ​​de ambiente para ajustar o comportamento da sua função sem atualizar o código.

**Versões**  
Gerencie a implantação de suas funções com versões, para que, por exemplo, uma nova função possa ser usada para testes beta sem afetar os usuários da versão de produção estável.

**Camadas**  
Empacote bibliotecas e outras dependências para reduzir o tamanho dos arquivos de implantação e tornar mais rápida a implantação do seu código.

**Fonte:** Documentação oficial AWS
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
1. Execução do exercício "Contador de Palavras" com Spark.  
![spark](/Sprint7/Exercicios/Spark/spark1.png)  
![spark](/Sprint7/Exercicios/Spark/spark2.png)  
![spark](/Sprint7/Exercicios/Spark/spark3.png)  
![spark](/Sprint7/Exercicios/Spark/spark4.png)  

2. Execução do exercício sobre a API do TMDB.  
![tmdb](/Sprint7/Exercicios/TMDB/tmdb_codigo.png)
![tmdb](/Sprint7/Exercicios/TMDB/tmdb_retorno.png)



# Links
[📜**Certificados**](/Sprint7/Certificados/)  
[🕵️‍♂️**Evidências** ](/Sprint7/Evidencias/)  
[💪**Exercícios**](/Sprint7/Exercicios/)  
[🖳 **Desafio**](/Sprint7/Desafio/README.md)  