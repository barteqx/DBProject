from sqlalchemy import Column, Integer, String, ForeignKey
from src.database.base_model import BaseModel

class User(BaseModel):

    __tablename__ = 'user'

    id          = Column(Integer, primary_key=True, nullable=False)
    email       = Column(String, nullable=False, unique=True)
    password    = Column(String, nullable=False)
    role        = Column(Integer, nullable=False)
    citizen_id  = Column(Integer, ForeignKey("citizen.id"), unique=True, nullable=False)


    def __repr__(self):
        return "<Uer: id = %d  email = %s  password = %s  role = %d  citizen_id = %d" % (
            self.id, self.email, self.password, self.role, self.citizen_id
        )
