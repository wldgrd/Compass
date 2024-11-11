/*Apresente a query para listar o código e o nome do vendedor com maior número de vendas (contagem), 
e que estas vendas estejam com o status concluída.  As colunas presentes no resultado devem ser, portanto, cdvdd e nmvdd.*/

SELECT 
	v.cdvdd,
	ven.nmvdd
FROM tbvendas v LEFT JOIN tbvendedor ven on v.cdvdd = ven.cdvdd 
WHERE v.status = 'Concluído'
GROUP BY ven.nmvdd
ORDER BY count(*) DESC
LIMIT 1