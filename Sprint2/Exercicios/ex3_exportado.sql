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