SELECT 
    l.cod AS CodLivro,
    l.titulo AS Titulo,
    a.codAutor AS CodAutor,
    a.nome AS NomeAutor,
    l.valor AS Valor,
    e.codEditora AS CodEditora,
    e.nome AS NomeEditora
FROM 
    livro l LEFT JOIN autor a ON l.autor = a.codAutor
	LEFT JOIN editora e ON l.editora = e.codEditora
ORDER BY 
    l.valor DESC
LIMIT 10;