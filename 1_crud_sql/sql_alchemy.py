from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import String, Column, Integer

engine = create_engine('postgresql://myuser:mypassword@localhost/mydb')

class Base(DeclarativeBase): pass

class Author(Base):
    __tablename__ = 'author1'
    author_id = Column(Integer, primary_key=True)
    name_author = Column(String(250), nullable=False)

Base.metadata.create_all(engine)
print('ok')