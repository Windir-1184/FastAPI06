# class que vai servir de modelo para gerar 
# a tabela aluno no database escola

from core.configs import settings
from sqlalchemy import Column, String, Integer, Float

class AlunoModel(settings.DBBaseModel):
    __tablename__= "alunos"
    matricula: int = Column(Integer, primary_key=True, autoincrement=True)
    nome: str = Column(String(120), nullable=False)
    idade: int = Column(Integer, nullable=False)
    nota: float = Column(Float, nullable=False)