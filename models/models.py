from sqlalchemy import MetaData, Integer, String, Text, Table, Column, create_engine, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import dotenv_values

config = dotenv_values(".env")

engine = create_engine(f"postgresql+psycopg2://{config['DB_USER']}:{config['DB_PASSWORD']}" + 
                       f"@{config['DB_HOST']}:{config['DB_PORT']}/{config['DB_NAME']}")
metadata = MetaData()
tbl = Table(
        "questions",
        metadata,
        Column("id", Integer, primary_key=True),
        Column("Text", String),
        Column("answer", String),
        Column("created_at", DateTime)
)
metadata.create_all(engine)

Base = declarative_base()

class Question(Base):
    __tablename__ = 'questions'
    id = Column(Integer, primary_key=True)
    question = Column(String)
    answer = Column(String)
    created_at = Column(DateTime)


Session = sessionmaker(bind=engine)


def save_question(question: Question) -> bool:
    session = Session()
    
    if session.query(Question).filter(Question.question == question.question).first() is not None:
        print("exists")
        session.commit()
        return False
    
    session.add(question)
    session.commit()
    session.close()

    return True