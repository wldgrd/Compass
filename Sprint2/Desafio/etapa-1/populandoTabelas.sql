
/*-------------------------------------------------------------------------------------*/

INSERT OR IGNORE INTO Carro (idCarro, kmCarro, classiCarro, marcaCarro, modeloCarro, anoCarro, idcombustivel ) -- Comando 'OR IGNORE' utilizado para que sejam inseridas apenas as chaves que não existem na tabela
SELECT 
	DISTINCT idCarro, 
	kmCarro, 
	classiCarro, 
	marcaCarro, 
	modeloCarro, 
	anoCarro, 
	idcombustivel 
FROM tb_locacao 

SELECT * -- verificando se foram feitas as inserções na tabela Carro
FROM Carro c 
ORDER BY idCarro 

/*-------------------------------------------------------------------------------------*/

INSERT INTO Cliente (idCliente, nomeCliente, cidadeCliente, estadoCliente, paisCliente)
SELECT
	DISTINCT idCliente, 
	nomeCliente, 
	cidadeCliente, 
	estadoCliente, 
	paisCliente
FROM tb_locacao 

SELECT * -- verificando se foram feitas as inserções na tabela Cliente
FROM Cliente
ORDER BY idCliente 

/*-------------------------------------------------------------------------------------*/

INSERT INTO Combustivel (idcombustivel, tipoCombustivel)
SELECT
	DISTINCT idcombustivel, 
	tipoCombustivel
FROM tb_locacao 

SELECT * -- verificando se foram feitas as inserções na tabela Combustível
FROM Combustivel 
ORDER BY idcombustivel

/*-------------------------------------------------------------------------------------*/

INSERT INTO Locacao (idLocacao, dataLocacao, horaLocacao, qtdDiaria, vlrDiaria, dataEntrega, horaEntrega, idCliente, idVendedor, idCarro, idcombustivel)
SELECT
	DISTINCT idLocacao, 
	dataLocacao, 
	horaLocacao, 
	qtdDiaria, 
	vlrDiaria, 
	dataEntrega, 
	horaEntrega, 
	idCliente, 
	idVendedor, 
	idCarro, 
	idcombustivel
FROM tb_locacao 

SELECT * -- verificando se foram feitas as inserções na tabela Locacao
FROM Locacao
ORDER BY idLocacao

/*-------------------------------------------------------------------------------------*/

INSERT INTO Vendedor (idVendedor, nomeVendedor, sexoVendedor, estadoVendedor)
SELECT
	DISTINCT idVendedor, 
	nomeVendedor, 
	sexoVendedor, 
	estadoVendedor
FROM tb_locacao 

SELECT * -- verificando se foram feitas as inserções na tabela Vendedor
FROM Vendedor v 
ORDER BY idVendedor 