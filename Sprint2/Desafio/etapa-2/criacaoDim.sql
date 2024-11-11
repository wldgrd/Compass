DROP TABLE tabelaFato; -- derrubar tabela caso existe para fazer os testes

CREATE TABLE tabelaFato( -- criação da tabela tabelaFato
	idCliente 	INT			NOT NULL,
	idVendedor 	INT 		NOT NULL,
	idCarro 	INT 		NOT NULL,
	dataLocacao DATE 		NOT NULL,
	horaLocacao TIME 		NOT NULL,
	dataEntrega DATE 		NOT NULL,
	horaEntrega TIME 		NOT NULL,
	qtdDiaria 	INT			NOT NULL,
	vlrDiaria 	DECIMAL		NOT NULL,
	PRIMARY KEY (idCliente,idVendedor,idCarro,dataLocacao) -- chave primária composta
	FOREIGN KEY (idCliente) 	REFERENCES dim_cliente(id), -- chave estrangeira para ligar a tabela dim_cliente à tabelaFato
    FOREIGN KEY (idVendedor) 	REFERENCES dim_vendedor(id), -- chave estrangeira para ligar a tabela dim_vendedor à tabelaFato
    FOREIGN KEY (idCarro) 		REFERENCES dim_carro(id), -- chave estrangeira para ligar a tabela dim_carro à tabelaFato
    FOREIGN KEY (idCarro)		REFERENCES dim_data(id) -- chave estrangeira para ligar a tabela dim_data à tabela fato
);

/*-------------------------------------------------------------------------------------*/

DROP TABLE dim_cliente;

CREATE TABLE dim_cliente(
    id       INT PRIMARY KEY 	NOT NULL, -- chave primária, identificador único
    nome     VARCHAR(100) 		NOT NULL,
    cidade   VARCHAR(40) 		NOT NULL,
    estado   VARCHAR(40) 		NOT NULL,
    pais     VARCHAR(40) 		NOT NULL
);

/*-------------------------------------------------------------------------------------*/

DROP TABLE dim_carro;

CREATE TABLE dim_carro(
	id         		INT 		PRIMARY KEY 		NOT NULL, -- chave primária, identificador único
    km         		INT 							NOT NULL,
    classi     		VARCHAR(50) 					NOT NULL,
    marca      		VARCHAR(80) 					NOT NULL,
    modelo     		VARCHAR(80) 					NOT NULL,
    ano        		INT 							NOT NULL,
    idcombustivel   INT 							NOT NULL,
    tipoCombustivel VARCHAR(20) 					NOT NULL
);

/*-------------------------------------------------------------------------------------*/

DROP TABLE dim_vendedor;

CREATE TABLE dim_vendedor(
    id      INT 		PRIMARY KEY NOT NULL, -- chave primária, identificador único
    nome    VARCHAR(15) 			NOT NULL,
    sexo    SMALLINT 				NOT NULL,
    estado  VARCHAR(40) 			NOT NULL	
);

/*-------------------------------------------------------------------------------------*/

DROP TABLE dim_data;

CREATE TABLE dim_data(
	id 						INT 		NOT NULL, --ID DO CARRO
	dataLocacao 			DATE 		NOT NULL,
	diaLocacao				INT			,
	mesLocacao				INT			,
	anoLocacao				INT			,
	horaLocacao 			TIME 		NOT NULL,
	dataEntrega 			DATE 		NOT NULL,
	horaEntrega 			TIME 		NOT NULL,
	diaEntrega 				INT			,
	mesEntrega				INT			,
	anoEntrega				INT			,
	PRIMARY KEY (id, dataLocacao) -- chave primária composta
);

/*-------------------------------------------------------------------------------------*/
