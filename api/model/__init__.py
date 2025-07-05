from sqlalchemy.orm import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

# Configurar a sessão do SQLAlchemy
Session = sessionmaker()

# Função para inicializar o banco de dados
async def init_db():
    from . import usuario  # Importar todos os modelos aqui
    engine = create_engine('sqlite:///database.db')
    Base.metadata.create_all(engine)
    Session.configure(bind=engine)