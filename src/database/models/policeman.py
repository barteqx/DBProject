from sqlalchemy import Integer
from src.database.base_model import BaseModel

class Policeman(BaseModel):

    __tablename__ = 'policeman'

    id = Column(Integer, primary_key=True, nullable=False)
    degree = Column(Integer, nullable=False)
    citizen_id = Column(Integer, ForeignKey("citizen.id"), nullable=False, unique=True)


    def __repr__(self):
        return "<Policeman: id = %d  degree = %d  citizen_id = %d>" % (
            self.id, self.degree, self.citizen_id
        )