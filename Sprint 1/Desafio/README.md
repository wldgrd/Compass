# Etapas do Desafio  


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
    
    
    

**Etapa II**  
O objetivo da segunda etapa do desafio é configurar o agendamento automático para que a execução do script processamento_de_vendas.sh seja feita por 4 dias seguidos. <br><br>

**Os procedimentos que o script deve fazer são os seguintes:**  
- Criar um agendamento de execução de comandos Linux para que o script _processamento_de_vendas.sh rode durante 4 dias seguidos às 15h27min  
```
crontab -e
```  
O comando crontab -e abre o editor de texto para que se possa adicionar a linha de comando referente ao agendamento.  
Para atender a solicitação de rodar por 4 dias, foi utilizada a seguinte linha de código:    

```  
27 15 * * 2-5 /home/welder/Documents/ecommerce/processamento_de_vendas.sh > /home/welder/Documents/ecommerce/logexec.txt 2>&1
```  

- Descrição da sintaxe da linha de código adicionada no serviço de agendamento:  

    - O comando acima significa que 27 minutos após a hora 15 (15h27min) o serviço cron executará o script  
    - "* *" : o primeiro * significa que será executado em qualquer dia do mês e o segundo * significa que será executado em qualquer mês    
    - 2-5: será executado de terça até quinta-feira
    - /home/welder/Documents/ecommerce/processamento_de_vendas.sh : caminho para o script que será executado  
    - **>** : redireciona a saída padrão   
    - /home/welder/Documents/ecommerce/logexec.txt 2>&1 : tanto a saída de execução normal quanto os erros serão enviados ao arquivo logexec.txt (essa etapa não foi solicitada no desafio, porém ajuda a verificar se o script foi executado de modo correto.)


**Etapa Final**  
O objetivo da etapa final é criar o script consolidador_de_processamento_de_vendas.sh que vai gerar o relatório final de vendas.  

**Os procedimentos que o script deve fazer são os seguintes:**  


- Modificar manualmente, todos os dias, os dados do arquivo dados_de_vendas.csv inserindo ou retirando linhas.  

- Criar um segundo Script chamado consolidador_de_processamento_de_vendas.sh que una todos os relatórios gerados anteriormente em um único arquivo chamado relatório_final.txt  
Para a criação do script consolidador_de_processamento_de_vendas.sh foi usado o código:  

```
echo "Relatório Final" > relatorio_final.txt   

cat vendas/backup/relatorio-*.txt > relatorio_final.txt
```  
- Descrição das linhas do código:

    - echo "Relatório Final" > relatorio_final.txt : Cria o arquivo relatorio_final.txt e escreve Relatório Final dentro dele
    - cat vendas/backup/relatorio-*.txt > relatorio_final.txt : Pega todos os arquivos cujo nome começa com relatorio- e que possuem a extensão .txt e adiciona seu conteúdo ao arquivo relatorio final.  





