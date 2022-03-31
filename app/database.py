from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from .config import setting

# "postgresql://<username>:<password>@<hostname>:<port>/<database_name>"
# SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"

SQLALCHEMY_DATABASE_URL = f"postgresql://{setting.database_username}:{setting.database_password}@{setting.database_host}:{setting.database_port}/{setting.database_name}"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
