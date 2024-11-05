/*Apresente a query para listar o código e nome cliente com maior gasto na loja. 
As colunas presentes no resultado devem ser cdcli, nmcli e gasto, esta última representando o 
somatório das vendas (concluídas) atribuídas ao cliente.*/


SELECT
	v.cdcli,
	v.nmcli,
	SUM(v.qtd*v.vrunt) as gasto
FROM tbvendas v LEFT JOIN tbestoqueproduto e on v.cdpro = e.cdpro 
GROUP BY v.nmcli 
ORDER BY gasto DESC 
LIMIT 1