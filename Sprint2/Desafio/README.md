# 1) OBJETIVO
	O objetivo é a prática de conhecimento de modelagem de dados Relacional e Dimensional com linguagem SQL.

# 2) ETAPAS DO DESAFIO  
**1) NORMALIZAR BASE DE DADOS**  
 - Aplicar as formas normais à tabela tb_locacao e criar um modelo relacional usando as tabelas normalizadas criadas.
 O código para a criação e população das tabelas está na pasta [etapa-1](/Sprint2/Desafio/etapa-1/).  

 **2) MODELO DIMENSIONAL BASEADO NO MODELO RELACIONAL**  
- Aqui pratiquei os conceitos de modelagem dimensional que estudei anteriormente. Estamos considerando a base de dados Concessionária, cujo modelo relacional foi criado na etapa anterior.  
- O desafio é montar o modelo dimensional com base no modelo relacional gerado anteriormente.   
- Apliquei as ideias aprendidas e gerei os arquivos .SQL na pasta [etapa-2](/Sprint2/Desafio/etapa-2/) para a criação e população das tabelas do modelo dimensional.  

A tabela original recebida para o desafio foi a ilustrada na figura abaixo.  
![](/Sprint2/evidencias/tabelaOriginal.png)  

O desafio foi criar um modelo **relacional** normalizado. Aqui apresento um modelo que julgo normalizado, porém para um próximo update poderia criar mais tabelas e separar outras entidades que acabei percebendo durante o processo.

O critério usado para normalizar foi seguir as 3 formas normais estudadas seguindo a seguinte lógica de relacionamentos:  

**Entidades Vendedor e Locação:**   
	Cada locação é realizada por um único vendedor,logo, a coluna idVendedor contida na tabela Locacao será usada como chave estrangeira que faz referência à coluna idVendedor da tabela Vendedor.  

**Entidades Carro e Locação:**   
	Cada locação um único carro, logo, a coluna idCarro da tabela Locacao será chave estrangeira que faz referência à coluna idCarro da tabela Carro.

**Entidades Combustível e Carro:**  
	O tipo de combustível usado por cada carro e registrado em cada locação deve ser descrito na tabela Combustivel. Logo, a coluna idcombustivel nas tabelas Carro e Locacao será chave estrangeira que faz referência à coluna idcombustivel da tabela Combustivel.

**Entidades Cliente e Locação:**  
	Uma locação é associada a um cliente único, logo, a coluna idCliente da tabela Locacao será chave estrangeira que faz referência à coluna idCliente da tabela Cliente.

Já no modelo **dimensional** a ideia é que ele seja otimizado para consultas rápidas e, por isso, aqui permite-se redundância de dados nas tabelas a fim de evitar múltiplos JOINS que diminuem a rapidez da consulta.   

Nessa parte da modelagem, leva-se em conta o chamado **star schema**, no qual a tabela fato vai no meio e ao redor são ligadas as dimensões pertinentes. A ideia é que na tabela fato contenham apenas informações numéricas, ou seja, dados que possam ser metrificados. No mais, o modelo recombina carro e combustível e acrescenta a tabela **dim_data** que tem por objetivo facilitar os filtros na execução das queries. Na dimensão data, temos separados os dias, meses e anos, tanto de locação quanto de entrega, facilitando assim a criação de algumas colunas calculadas e possíveis manipulações que possam vir a ser feitas.  

O resultado dessas construções pode ser observado na pasta [**evidências**](/Sprint2/evidencias/README.md)










