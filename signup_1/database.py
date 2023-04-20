from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine("mysql://root:root@localhost:3306/lucky")
SessionLocal = sessionmaker(bind=engine,autoflush=False)
Base= declarative_base()

