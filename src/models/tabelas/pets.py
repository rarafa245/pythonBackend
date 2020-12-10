import enum
from sqlalchemy import Column, Integer, String, Enum, ForeignKey
from src.models.db_settings import Base

class Pets(Base):
    __tablename__ = 'pets'

    class Tipos_de_animais(enum.Enum):
        # Definindo os tipos de Pets disponiveis
        cachorro = 'cachorro'
        gato = 'gato'
        peixe = 'peixe'
        tartaruga = 'tartaruga'

    id = Column(Integer, primary_key=True)
    nome = Column(String(20))
    tipo = Column(Enum(Tipos_de_animais))
    idade = Column(Integer)
    usuario_id = Column(Integer, ForeignKey('usuarios.id'))
