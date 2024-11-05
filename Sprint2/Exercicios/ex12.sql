/*Apresente a query para listar código, nome e data de nascimento dos dependentes do vendedor com 
menor valor total bruto em vendas (não sendo zero). As colunas presentes no resultado devem ser 
cddep,nmdep, dtnasc e valor_total_vendas.

Observação: Apenas vendas com status concluído.*/


SELECT 
	d.cddep ,
	d.nmdep,
	d.dtnasc,
	SUM(v.qtd * v.vrunt) as valor_total_vendas
FROM tbvendas v LEFT JOIN tbestoqueproduto e on v.cdpro = e.cdpro 
	 LEFT JOIN tbvendedor vend on v.cdvdd = vend.cdvdd 
	 LEFT JOIN tbdependente d on vend.cdvdd = d.cdvdd 
WHERE v.status = 'Concluído'
GROUP BY vend.cdvdd 
ORDER BY valor_total_vendas 
LIMIT 1