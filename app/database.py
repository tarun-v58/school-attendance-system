import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

# 1. Load the secret variables from the .env file into Python's environment
load_dotenv()

USER = os.getenv("DB_USER")
PASSWORD = os.getenv("DB_PASSWORD")
HOST = os.getenv("DB_HOST")
PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")

# 2. Build the database connection URL
DATABASE_URL = f"postgresql://{USER}:{PASSWORD}@{HOST}:{PORT}/{DB_NAME}"

# 3. Create the SQLAlchemy Engine
engine = create_engine(DATABASE_URL)

# 4. Create the Session factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 5. Base class for our database models to inherit from
Base = declarative_base()

# 6. Database session generator for our API routes
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()