import sqlite3

# Conectar ao banco de dados (ou criá-lo se não existir)
conn = sqlite3.connect('recrutamento.db')

# Criar um cursor
cursor = conn.cursor()

# Criar a tabela Desenvolvedor
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Desenvolvedor (
        ID_dev INTEGER PRIMARY KEY,
        Nome TEXT,
        Endereco TEXT,
        E_mail TEXT,
        Curriculo BLOB,
        Formacao TEXT,
        Habilidades TEXT,
        Atributo_1 TEXT
    )
''')

# Criar a tabela Recrurador (corrigindo o nome da tabela para Recrutador)
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Recrutador (
        ID_REC INTEGER PRIMARY KEY,
        Nome TEXT,
        Setor TEXT,
        Localizacao TEXT,
        Descricao TEXT,
        Contato INTEGER
    )
''')

# Criar a tabela Vagas
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Vagas (
        ID_Vaga INTEGER PRIMARY KEY,
        Titulo TEXT,
        Descricao TEXT,
        Empresa TEXT,
        Localizacao TEXT,
        Salario REAL,
        Requisitos TEXT,
        Data DATE,
        fk_Recrurador_ID_REC INTEGER,
        FOREIGN KEY (fk_Recrurador_ID_REC) REFERENCES Recrutador (ID_REC) ON DELETE CASCADE
    )
''')

# Criar a tabela Candidata
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Candidata (
        fk_Desenvolvedor_ID_dev INTEGER,
        fk_Vagas_ID_Vaga INTEGER,
        Status TEXT,
        FOREIGN KEY (fk_Desenvolvedor_ID_dev) REFERENCES Desenvolvedor (ID_dev) ON DELETE SET NULL,
        FOREIGN KEY (fk_Vagas_ID_Vaga) REFERENCES Vagas (ID_Vaga) ON DELETE SET NULL
    )
''')

# Commit as alterações e fechar a conexão
conn.commit()
conn.close()
