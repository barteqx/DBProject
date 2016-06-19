from sqlalchemy import Column, Integer
from src.database.base_model import BaseModel

class Cell(BaseModel):

    __tablename__ = 'cell'

    id      = Column(Integer, primary_key=True, nullable=False)
    number  = Column(Integer, nullable=False, unique=True)

    def __repr__(self):
        return "<Cell: id = %d  number = %d>" % (
            self.id, self.number
        )