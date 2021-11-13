from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import create_engine
import os


engine = create_engine(
    f"postgresql://{os.environ.get('DB_USER')}:{os.environ.get('DB_PASSWORD')}@localhost/{os.environ.get('DB_NAME')}",
    echo=True
)
Base = declarative_base()
SessionLocal = sessionmaker(bind=engine)
