/*Apresente a query para listar o autor com maior número de livros publicados. 
O resultado deve conter apenas as colunas codautor, nome, quantidade_publicacoes.*/

select
	a.codautor,
	a.nome,
	count(l.publicacao) as quantidade_publicacoes
FROM livro l LEFT JOIN autor a on l.autor = a.codautor 
GROUP BY a.nome 
ORDER BY quantidade_publicacoes DESC
LIMIT 1