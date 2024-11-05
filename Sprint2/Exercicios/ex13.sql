/*Apresente a query para listar os 10 produtos menos vendidos pelos canais de E-Commerce ou Matriz 
(Considerar apenas vendas concluídas).  
As colunas presentes no resultado devem ser cdpro, nmcanalvendas, nmpro e quantidade_vendas.*/

SELECT
	v.cdpro,
	v.nmcanalvendas ,
	v.nmpro,
	SUM(v.qtd) as quantidade_vendas
FROM tbvendas v 
WHERE ( v.status = 'Concluído' ) AND (v.nmcanalvendas in ('Matriz', 'Ecommerce') )
GROUP BY v.nmpro , v.nmcanalvendas 
ORDER BY quantidade_vendas 
LIMIT 10