from typing import Optional
from pydantic import BaseModel as SCBaseModel

class AlunoSchema(SCBaseModel):
    matricula: Optional[int] = None
    nome: str
    idade: int
    nota: float

    class Config:
        orm_mode = True #garante a conversao entre tipos de aluno models pra aluno schema

#class AlunoSchema serve de modelo para envio e receimento atráves da API