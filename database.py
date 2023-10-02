from sqlalchemy import create_engine
from models import Base

DATABASE_URL = "sqlite:///./record.db"

engine = create_engine(DATABASE_URL, echo=True)

# Create SQL schemas if they don't exist already
Base.metadata.create_all(engine)