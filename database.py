from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# SQLite DB
engine = create_engine("sqlite:///chat.db")
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()

# Chat model
class Chat(Base):
    __tablename__ = "chats"
    id = Column(Integer, primary_key=True, index=True)
    question = Column(String, nullable=False)
    answer = Column(String, nullable=False)

# Create table
Base.metadata.create_all(bind=engine)