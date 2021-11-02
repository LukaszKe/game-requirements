from sqlalchemy import Column, String, Integer, Float
from database.base import Base


class GPU(Base):
    __tablename__ = 'GPU'

    name = Column(String, primary_key=True)
    gpu_mark = Column(Integer)
    price = Column(Float)
