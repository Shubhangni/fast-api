from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
# Database URI
db_url = "sqlite:///./my_database.db"
# Create an engine
engine = create_engine(db_url, echo=True, connect_args={"check_same_thread": False} ) # for debugging purposes
# Create a connection
Base = declarative_base()
sessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = sessionLocal()
    try:
        yield db
    finally:
        db.close()
                       