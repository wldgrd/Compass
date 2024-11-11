SELECT 
	v.cdvdd,
	ven.nmvdd
FROM tbvendas v LEFT JOIN tbvendedor ven on v.cdvdd = ven.cdvdd 
WHERE v.status = 'Concluído'
GROUP BY ven.nmvdd
ORDER BY count(*) DESC
LIMIT 1