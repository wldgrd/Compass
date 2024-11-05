/*Apresente a query para listar o nome dos autores que 
publicaram livros através de editoras NÃO situadas na 
região sul do Brasil. Ordene o resultado pela coluna nome, 
em ordem crescente. Não podem haver nomes repetidos em seu 
retorno.*/


SELECT 
	a.nome
FROM livro l LEFT JOIN autor a on l.autor = a.codautor 
	LEFT JOIN editora e on l.editora = e.codeditora 
	LEFT JOIN endereco en on e.endereco = en.codendereco 
WHERE en.estado <> 'PARANÁ'
group by a.nome
order by a.nome