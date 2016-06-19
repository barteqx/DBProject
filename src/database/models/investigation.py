from sqlalchemy import Column, Integer, String, ForeignKey, Date
from src.database.base_model import BaseModel

class Investigation(BaseModel):

    __tablename__ = 'investigation'

    id              = Column(Integer, primary_key=True, nullable=False)
    status          = Column(Integer, nullable=False)
    start_date      = Column(Date, nullable=False)
    closed_date     = Column(Date)
    description     = Column(String(255))
    policeman_id    = Column(Integer, ForeignKey("policeman.id"))


    def __repr__(self):
        return "<Investigation: id = %d  status = %d  start_date = %s  closed_date = %s  description = %s policeman_id = %d" % (
            self.id, self.status, self.start_date, self.closed_date, self.description, self.policeman_id
        )
