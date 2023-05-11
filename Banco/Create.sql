CREATE TABLE aluno (
    id INTEGER PRIMARY KEY,
    dadosId INTEGER,
    nome TEXT NOT NULL,
    email TEXT NOT NULL,
    celular TEXT NOT NULL,
    dtNascimento DATE NOT NULL,
    senha TEXT NOT NULL,
    endereco TEXT,
    FOREIGN KEY(dadosId)
        REFERENCES dadosAluno(id) 
)

CREATE TABLE instrutor(
    id INTEGER PRIMARY KEY,
    nome TEXT NOT NULL,
    email TEXT NOT NULL,
    celular TEXT NOT NULL,
    endereco TEXT,
    academia INTEGER, 
    FOREIGN KEY(academia) 
        REFERENCES academia (id)
)

CREATE TABLE academia(
    id INTEGER PRIMARY KEY,
    nome TEXT NOT NULL,
    email TEXT NOT NULL,
    celular TEXT NOT NULL,
    endereco TEXT,
    siteDomain TEXT,
    CNPJ INTEGER
)

CREATE TABLE dadosAluno(
    id INTEGER PRIMARY KEY,
    frequencia INTEGER,
    tempo INTEGER,
    peso INTEGER  NOT NULL,
    altura INTEGER NOT NULL,
    objetivos INTEGER,
    academia INTEGER, 
    instrutor INTEGER,
    FOREIGN KEY(academia) 
        REFERENCES academia (id),
    FOREIGN KEY(instrutor) 
        REFERENCES instrutor (id),
    FOREIGN KEY (objetivos)
        REFERENCES objetivo (id)
)

CREATE TABLE objetivo(
    id INTEGER PRIMARY KEY,
    peso REAL, 
    massaMuscular REAL,
    gorduraCorporal REAL,
    aguaCorporal REAL,
    tipo TEXT,
    evolucao REAL
)
CREATE TABLE grupoMuscular(
    id INTEGER PRIMARY KEY,
    nome TEXT
)

CREATE TABLE exercicios(
    id INTEGER PRIMARY KEY,
    nome TEXT,
    grupo INTEGER, 
    FOREIGN KEY (grupo)
        REFERENCES grupoMuscular(Id)
)

CREATE TABLE exercicioTreino(
    id INTEGER PRIMARY KEY,
    exercicio INTEGER,
    repeticao INTEGER,
    peso INTEGER,
    series INTEGER,
    FOREIGN KEY (exercicio)
        REFERENCES exercicios (Id)
)

CREATE TABLE treinoDiario(
    id INTEGER PRIMARY KEY,
    dia DATE,
    executado INTEGER,
    exercicio INTEGER,
    FOREIGN KEY (exercicio)
        REFERENCES exercicioTreino (Id)
)

CREATE TABLE treino(
    treinoDiario INTEGER,
    dataInicio DATE,
    dataFim DATE,
    aluno INTEGER,
    FOREIGN KEY(aluno)
        REFERENCES aluno (Id),
    FOREIGN KEY(treinoDiario)
        REFERENCES treinoDiario (Id)
)