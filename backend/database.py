import os
from sqlmodel import SQLModel, create_engine, Session

# Define que localmente usaremos o SQLite (cria o arquivo db.sqlite3 automaticamente)
DATABASE_URL = "sqlite:///./db.sqlite3"

# O 'engine' é a ponte de comunicação com o banco de dados
engine = create_engine(
    DATABASE_URL, 
    connect_args={"check_same_thread": False}  # Necessário apenas para o SQLite rodar com o FastAPI
)

def criar_banco_e_tabelas():
    # Lê todos os modelos criados e cria as tabelas físicas no banco
    SQLModel.metadata.create_all(engine)

def get_session():
    # Abre e fecha conexões com o banco de dados de forma segura a cada requisição
    with Session(engine) as session:
        yield session
