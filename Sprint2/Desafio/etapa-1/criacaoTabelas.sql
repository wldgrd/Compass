/*-------------------------------------------------------------------------------------*/
DROP TABLE Vendedor;
CREATE TABLE Vendedor ( -- cria a tabela Vendedor
    idVendedor      INT PRIMARY KEY NOT NULL, -- chave primária, identificador único
    nomeVendedor    VARCHAR(15) 	NOT NULL,
    sexoVendedor    SMALLINT 		NOT NULL,
    estadoVendedor  VARCHAR(40) 	NOT NULL
)

/*-------------------------------------------------------------------------------------*/
DROP TABLE Carro;
CREATE TABLE Carro ( -- cria a tabela Carro
    idCarro         INT PRIMARY KEY NOT NULL, -- chave primária, identificador único
    kmCarro         INT 			NOT NULL,
    classiCarro     VARCHAR(50) 	NOT NULL,
    marcaCarro      VARCHAR(80) 	NOT NULL,
    modeloCarro     VARCHAR(80) 	NOT NULL,
    anoCarro        INT 			NOT NULL,
    idcombustivel   INT 			NOT NULL,
    FOREIGN KEY (idcombustivel) REFERENCES Combustivel(idcombustivel) -- chave estrangeira para fazer a ligação entre as tabelas Carro e Combustível
)

/*-------------------------------------------------------------------------------------*/
DROP TABLE Locacao;
CREATE TABLE Locacao ( -- criação da tabela Locacao
    idLocacao       INT PRIMARY KEY NOT NULL, -- chave primária, identificador único
    dataLocacao     DATE 			NOT NULL,
    horaLocacao     TIME 			NOT NULL,
    qtdDiaria       INT 			NOT NULL,
    vlrDiaria       DECIMAL(18,2) 	NOT NULL,
    dataEntrega     DATE 			NOT NULL,
    horaEntrega     TIME 			NOT NULL,
    idCliente       INT 			NOT NULL,
    idVendedor      INT 			NOT NULL,
    idCarro         INT 			NOT NULL,
    idcombustivel   INT 			NOT NULL,
    FOREIGN KEY (idCliente) REFERENCES Cliente(idCliente), -- chave estrangeira para fazer a ligação entre as tabelas Cliente e Locação
    FOREIGN KEY (idVendedor) REFERENCES Vendedor(idVendedor), -- chave estrangeira para fazer a ligação entre as tabelas Vendedor e Locação 
    FOREIGN KEY (idCarro) REFERENCES Carro(idCarro) -- chave estrangeira para fazer a ligação entre as tabelas Carro e Locação
)

/*-------------------------------------------------------------------------------------*/
DROP TABLE Cliente;
CREATE TABLE Cliente (
    idCliente       INT PRIMARY KEY NOT NULL, -- chave primária, identificador único
    nomeCliente     VARCHAR(100) 	NOT NULL,
    cidadeCliente   VARCHAR(40) 	NOT NULL,
    estadoCliente   VARCHAR(40) 	NOT NULL,
    paisCliente     VARCHAR(40) 	NOT NULL
)

/*-------------------------------------------------------------------------------------*/
DROP TABLE Combustivel;
CREATE TABLE Combustivel (
    idcombustivel   INT PRIMARY KEY NOT NULL, -- chave primária, identificador único
    tipoCombustivel VARCHAR(20) 	NOT NULL
)

/*-------------------------------------------------------------------------------------*/

