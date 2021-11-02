from sqlalchemy import Column, String, Integer, Float
from database.base import Base


class CPU(Base):
    __tablename__ = 'CPU'

    name = Column(String, primary_key=True)
    cpu_mark = Column(Integer)
    price = Column(Float)
