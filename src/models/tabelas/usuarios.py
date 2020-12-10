from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from src.models.db_settings import Base

class Usuarios(Base):
    __tablename__ = 'usuarios'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    password = Column(String)
    id_pet = relationship('Pets')

    def __repr__(self):
        return f'Usuarios {self.name}'
