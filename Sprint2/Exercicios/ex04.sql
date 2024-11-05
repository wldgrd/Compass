/*Apresente a query para listar a quantidade de livros publicada por cada autor. 
Ordenar as linhas pela coluna nome (autor), em ordem crescente. 
Além desta, apresentar as colunas codautor, nascimento e quantidade (total de livros de sua autoria).*/

SELECT 
	a.nome,
	a.codautor ,
	a.nascimento ,
	count(l.titulo) as quantidade
FROM livro l FULL JOIN autor a on l.autor = a.codautor 
GROUP BY a.codautor 
ORDER BY a.nome ASC 