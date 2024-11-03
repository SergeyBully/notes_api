from sqlalchemy import Column, Integer, String, ForeignKey, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from ..core.config import DATABASE_URI


Base = declarative_base()


class Notes(Base):
    __tablename__ = 'notes'

    note_id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(255), nullable=False)
    content = Column(String, nullable=False)
    update_date = Column(Integer, nullable=False)
    type_id = Column(Integer, ForeignKey('types.type_id'), nullable=False)

class UpdateHistory(Base):
    __tablename__ = 'update_history'

    update_id = Column(Integer, primary_key=True, autoincrement=True)
    note_id = Column(Integer, ForeignKey('notes.note_id'), nullable=False)
    title = Column(String(255), nullable=False)
    content = Column(String, nullable=False)
    update_date = Column(Integer, nullable=False)
    type_id = Column(Integer, ForeignKey('types.type_id'), nullable=False)

class Types(Base):
    __tablename__ = 'types'

    type_id = Column(Integer, primary_key=True, autoincrement=True)
    type_name = Column(String(50), nullable=False)


# Create a database engine
engine = create_engine(DATABASE_URI)
Session = sessionmaker(bind=engine)

# Automatically create tables if they don't exist
Base.metadata.create_all(engine)