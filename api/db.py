from sqlmodel import create_engine, Session
import os 


DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://user:password@neon-host/dbname")

engine = create_engine(DATABASE_URL, echo=True)

def get_session():
    with Session(engine) as session:
        yield session