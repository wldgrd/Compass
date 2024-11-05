/*Apresente a query para listar o código e nome do produto mais vendido entre as datas de 2014-02-03 
até 2018-02-02, e que estas vendas estejam com o status concluída. 
As colunas presentes no resultado devem ser cdpro e nmpro.*/

SELECT 
	e.cdpro, 
	v.nmpro
FROM tbvendas v LEFT JOIN tbestoqueproduto e 
WHERE v.dtven BETWEEN '2014-02-03' AND '2018-02-03'
GROUP BY v.nmpro 
LIMIT 1