SELECT *
FROM Carro c 
ORDER BY idCarro 

SELECT *
FROM Cliente
ORDER BY idCliente 

SELECT *
FROM Combustivel 
ORDER BY idcombustivel 

SELECT *
FROM Vendedor v 
ORDER BY idVendedor 

/*-------------------------------------------------------------------------------------*/

INSERT OR IGNORE INTO Carro (idCarro, kmCarro, classiCarro, marcaCarro, modeloCarro, anoCarro, idcombustivel )
SELECT 
	DISTINCT idCarro, 
	kmCarro, 
	classiCarro, 
	marcaCarro, 
	modeloCarro, 
	anoCarro, 
	idcombustivel 
FROM tb_locacao 

/*-------------------------------------------------------------------------------------*/

INSERT INTO Cliente (idCliente, nomeCliente, cidadeCliente, estadoCliente, paisCliente)
SELECT
	DISTINCT idCliente, 
	nomeCliente, 
	cidadeCliente, 
	estadoCliente, 
	paisCliente
FROM tb_locacao 

/*-------------------------------------------------------------------------------------*/

INSERT INTO Combustivel (idcombustivel, tipoCombustivel)
SELECT
	DISTINCT idcombustivel, 
	tipoCombustivel
FROM tb_locacao 

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

/*-------------------------------------------------------------------------------------*/

INSERT INTO Vendedor (idVendedor, nomeVendedor, sexoVendedor, estadoVendedor)
SELECT
	DISTINCT idVendedor, 
	nomeVendedor, 
	sexoVendedor, 
	estadoVendedor
FROM tb_locacao 


