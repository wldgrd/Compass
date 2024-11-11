/*Apresente a query para listar o nome dos autores com nenhuma publicação. Apresentá-los em ordem crescente.*/

select
	a.nome
FROM livro l FULL JOIN autor a on l.autor = a.codautor 
GROUP BY a.nome 
HAVING count(l.titulo) = 0
ORDER BY a.nome

