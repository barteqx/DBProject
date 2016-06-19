from sqlalchemy import Column, Integer, String, Date
from src.database.base_model import BaseModel

class Citizen(BaseModel):

    __tablename__ = 'citizen'

    id          = Column(Integer, primary_key=True, nullable=False)
    name        = Column(String(50))
    surname     = Column(String(100))
    birth_date  = Column(Date)
    pesel       = Column(Integer, unique=True)

    def __repr__(self):
        return "<Citizen: id = %d  name = %s  surname = %s  birth_date = %s  pesel = %d>" % (
            self.id, self.name, self.surname, self.birth_date, self.pesel
        )
