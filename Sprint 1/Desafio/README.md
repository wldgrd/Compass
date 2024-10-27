# Instruções

Neste arquivo você apresentará suas entregas referentes ao desafio. Utilize o diretório "Desafio" para organizar seus artefatos e este README.md para fazer referência aos arquivos de código-fonte e demais entregáveis solicitados.

Esperamos que haja, minimamente:

- Passo a passo para obter o resultado entregue do desafio.
- Trechos de códigos e suas explicações.
- Relacionamento com a pasta de evidências (imagens).


# Etapas


**Etapa I**  
    O objetivo da primeira etapa do desafio é construir um script usando comandos Linux para executar uma sequência de criação, manipulação, compactação e remoção de alguns arquivos.  <br><br> 
**Os procedimentos que o script deve fazer são os seguintes:**

- Criar um diretório no linux chamado ecommerce e inserir o arquivo dados_de_vendas.csv  

- Criar um script chamado processamento_de_vendas.sh que realizará as seguintes funções:

    - Criar uma pasta chamada vendas e copiar o arquivo dados_de_vendas.csv para dentro dela

    - Criar dentro da pasta vendas uma subpasta chamada backup e colar uma cópia do arquivo dados_de_vendas.csv dentro dela

    - Trocar o nome do arquivo que está dentro da pasta vendas para dados-yyyymmdd.csv (yyyymmdd é respectivamente, o ano, mês e dia que o script foi executado. Ex: caso o script seja executado no dia 16/10/24, o nome do arquivo ficará: dados-20241016)

    - Repetir o passo anterior com o arquivo que está dentro da pasta backup, porém agora o nome do arquivo será: backup-dados-yyyymmdd.csv

    - Criar dentro da pasta backup um arquivo chamado relatório.txt que contenha a data e hora no formato YYYY/MM/DD HH:MM, data do primeiro registro de venda, data do último registro de venda, quantidade de itens diferentes vendidos e as dez primeiras linhas de produtos vendidos.  

    - Transformar o arquivo backup-dados-yyyymmdd.csv para backup-dados-yyyymmdd.zip  

    - Apagar o arquivo backup-dados-yyyymmdd.csv da pasta backup e o arquivo dados_de_vendas.csv da pasta vendas.  

[O código completo pode ser acessado clicando aqui.](/Sprint%201/Desafio/etapa-1/processamento_de_vendas.sh)  

    
O código usado para começar a primeira etapa e criar o diretório ecommerce:
    
    mkdir ecommerce #Cria o diretório ecommerce  
    
    
    

2. ... [Etapa II](etapa-2)

    Já com esse código, o objetivo é ...

    ```
    Esta é uma outra linha de código
    ```
    



