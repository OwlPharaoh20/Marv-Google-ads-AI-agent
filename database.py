# database.py
from sqlalchemy import Column, Integer, String, DateTime, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from datetime import datetime
import os
from dotenv import load_dotenv

load_dotenv()

MYSQL_URL = os.getenv("MYSQL_URL")
engine = create_engine(MYSQL_URL)
SessionLocal = sessionmaker(bind=engine)

Base = declarative_base()

class AdCampaign(Base):
    __tablename__ = "ad_campaigns"

    id = Column(Integer, primary_key=True, index=True)
    objective = Column(String(255))
    budget = Column(String(20))
    country = Column(String(100))
    status = Column(String(50))
    created_at = Column(DateTime, default=datetime.utcnow)

def init_db():
    Base.metadata.create_all(bind=engine)
