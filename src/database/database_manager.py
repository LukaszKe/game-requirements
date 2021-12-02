from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database.base import Base
from entity.gpu import GPU
from entity.cpu import CPU


class DatabaseManager:
    session: None

    def __init__(self):
        engine = create_engine('sqlite:///hardware.db', echo=True)
        Base.metadata.create_all(engine)  # create table

        self.session = sessionmaker(bind=engine)()

    def get_cpu_by_name(self, name):
        return self.session.query(CPU).get(name)

    def get_gpu_by_name(self, name):
        return self.session.query(GPU).get(name)

    def get_cpu_by_name_in(self, name):
        return self.session.query(CPU).filter(CPU.name.like(f'%{name}%')).first()
