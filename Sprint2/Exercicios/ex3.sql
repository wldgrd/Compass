/*apresente a query para listar as 5 editoras com mais livros na biblioteca. 
 O resultado deve conter apenas as colunas quantidade, nome, estado e cidade. 
 Ordenar as linhsa pela coluna que representa a quantidade de livros em ordem decrescente*/

SELECT 
	COUNT(ed.nome) as quantidade,
	ed.nome ,
	en.estado ,
	en.cidade 
from livro l LEFT JOIN editora ed on l.editora = ed.codeditora 
	LEFT JOIN endereco en on ed.endereco = en.codendereco 
group by ed.nome 
order by quantidade desc 
limit 5