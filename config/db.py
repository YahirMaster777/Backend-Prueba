from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
#configuracion de la base de datosm en Mysql
SQLALCHEMY_DATABASE_URL = "mysql+pymysql://root:1234@localhost:3306/prueba_back_db"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
