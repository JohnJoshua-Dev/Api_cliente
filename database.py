from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os


# Carregando os Arquivos dotenv
load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL")
TABLE= os.getenv("TABLE")

# Criacao do engine
engine = create_engine(DATABASE_URL)

# Criacao da sessao de conexao
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Criacao da base para modelos
Base = declarative_base()

# Dependecias para obter a sessao de banco
def get_db():
    db = SessionLocal()
    try:
        yield db

    finally:
        db.close()