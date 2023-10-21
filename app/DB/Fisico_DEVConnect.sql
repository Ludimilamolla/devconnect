/* Logico_DEVConnect: */

CREATE TABLE Desenvolvedor (
    ID_dev INTEGER PRIMARY KEY,
    Nome VARCHAR,
    Endereco VARCHAR,
    E_mail VARCHAR,
    Curriculo BLOB,
    Formacao VARCHAR,
    Habilidades VARCHAR,
    Atributo_1 VARCHAR
);

CREATE TABLE Recrurador (
    ID_REC INTEGER PRIMARY KEY,
    Nome VARCHAR,
    Setor VARCHAR,
    Localizacao VARCHAR,
    Descricao VARCHAR,
    Contato INTEGER
);

CREATE TABLE Vagas (
    ID_Vaga INTEGER PRIMARY KEY,
    Titulo VARCHAR,
    Descricao CLOB,
    Empresa VARCHAR,
    Localizacao VARCHAR,
    Salario FLOAT,
    Requisitos CLOB,
    Data DATE,
    fk_Recrurador_ID_REC INTEGER
);

CREATE TABLE Candidata (
    fk_Desenvolvedor_ID_dev INTEGER,
    fk_Vagas_ID_Vaga INTEGER,
    Status VARCHAR
);
 
ALTER TABLE Vagas ADD CONSTRAINT FK_Vagas_2
    FOREIGN KEY (fk_Recrurador_ID_REC)
    REFERENCES Recrurador (ID_REC)
    ON DELETE CASCADE;
 
ALTER TABLE Candidata ADD CONSTRAINT FK_Candidata_1
    FOREIGN KEY (fk_Desenvolvedor_ID_dev)
    REFERENCES Desenvolvedor (ID_dev)
    ON DELETE SET NULL;
 
ALTER TABLE Candidata ADD CONSTRAINT FK_Candidata_2
    FOREIGN KEY (fk_Vagas_ID_Vaga)
    REFERENCES Vagas (ID_Vaga)
    ON DELETE SET NULL;