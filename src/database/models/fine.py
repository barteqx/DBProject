from sqlalchemy import Column, Integer, ForeignKey, Date, Boolean, Time
from src.database.base_model import BaseModel

class Fine(BaseModel):

    __tablename__ = 'fine'

    id              = Column(Integer, primary_key=True, nullable=False)
    date            = Column(Date, nullable=False)
    time            = Column(Time, nullable=False)
    amount          = Column(Integer, nullable=False)
    paid            = Column(Boolean, nullable=False, default=False)
    policeman_id    = Column(Integer, ForeignKey("policeman.id"))
    citizen_id      = Column(Integer, ForeignKey("citizen.id"))

    def __repr__(self):
        return "<Fine: id = %d  date = %s  time = %s  amount = %d  paid = %b  policeman_id = %d  citizen_id = %d>" % (
            self.id, self.date, self.time, self.amount, self.paid, self.policeman_id, self.citizen_id
        )
