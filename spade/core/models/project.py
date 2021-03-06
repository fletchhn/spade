from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, ForeignKey, Integer, String, Binary

Base = declarative_base()

class ProjectInfo(Base):
    __tablename__ = "project_info"
    key = Column(String, nullable=False, primary_key=True)
    value = Column(String)

class ProjectFile(Base):
    __tablename__ = "project_files"
    path = Column(String, nullable=False, primary_key=True)
    sha256 = Column(Binary(32))
