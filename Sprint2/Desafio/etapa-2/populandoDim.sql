/*-------------------------------------------------------------------------------------*/

INSERT INTO tabelaFato (idCliente, idVendedor, idCarro, dataLocacao, horaLocacao, dataEntrega, horaEntrega, qtdDiaria, vlrDiaria)
SELECT 
	idCliente, 
	idVendedor, 
	idCarro, 
	dataLocacao, 
	horaLocacao, 
	dataEntrega, 
	horaEntrega, 
	qtdDiaria, 
	vlrDiaria
FROM Locacao 

SELECT * -- verificando se foram feitas as inserções na tabelaFato
FROM tabelaFato tf 

/*-------------------------------------------------------------------------------------*/

INSERT OR IGNORE INTO dim_carro (id, km, classi, marca, modelo, ano, idcombustivel, tipoCombustivel) -- aqui o comando 'OR IGNORE' foi usado para inserir apenas os IDs únicos 
SELECT
	cr.idCarro , 
	cr.kmCarro , 
	cr.classiCarro , 
	cr.marcaCarro , 
	cr.modeloCarro , 
	cr.anoCarro , 
	cr.idcombustivel, 
	cb.tipoCombustivel
FROM Carro cr LEFT JOIN Combustivel cb 

SELECT * -- verificando se foram feitas as inserções na tabela dim_carro
FROM dim_carro dc 

/*-------------------------------------------------------------------------------------*/

INSERT INTO dim_cliente (id, nome, cidade, estado, pais)
SELECT
	idCliente,
	nomeCliente ,
	cidadeCliente ,
	estadoCliente ,
	paisCliente 
FROM Cliente 

SELECT * -- verificando se foram feitas as inserções na tabela dim_cliente
FROM dim_cliente dc

/*-------------------------------------------------------------------------------------*/

INSERT INTO dim_vendedor (id, nome, sexo, estado)
SELECT
	idVendedor ,
	nomeVendedor ,
	sexoVendedor ,
	estadoVendedor 
FROM Vendedor 

SELECT * -- verificando se foram feitas as inserções na tabela dim_vendedor
FROM dim_vendedor dv 
/*-------------------------------------------------------------------------------------*/

INSERT INTO dim_data (id, dataLocacao, diaLocacao, mesLocacao, anoLocacao, horaLocacao, dataEntrega, horaEntrega, diaEntrega, mesEntrega, anoEntrega)
SELECT 
	idCarro , 
	dataLocacao,
	SUBSTR(REPLACE(dataLocacao, '.', ''), 7, 2) AS diaLocacao,
	SUBSTR(REPLACE(dataLocacao, '.', ''), 5, 2) AS mesLocacao,
	SUBSTR(REPLACE(dataLocacao, '.', ''), 1, 4) AS anoLocacao,
	horaLocacao, 
	dataEntrega, 
	horaEntrega, 
	SUBSTR(REPLACE(dataEntrega, '.', ''), 7, 2) AS diaEntrega,
	SUBSTR(REPLACE(dataEntrega, '.', ''), 5, 2) AS mesEntrega,
	SUBSTR(REPLACE(dataEntrega, '.', ''), 1, 4) AS anoEntrega
FROM Locacao 

/*OBS: as datas vieram formatadas com um '.' entre os valores e para que seja possível extrair o dia, mês e ano separadamente através do método SUBSTR
é preciso fazer a remoção do ponto para que então a data fique no formato YYYYMMDD e daí sim recortarmos as substrings correspondentes.*/

SELECT * -- verificando se foram feitas as inserções na tabela dim_data
FROM dim_data dd 

/*-------------------------------------------------------------------------------------*/
