from sqlalchemy import Column, Integer, String, ForeignKey, Date, Boolean
from src.database.base_model import BaseModel

class Arrest(BaseModel):

    __tablename__ = 'arrest'

    id              = Column(Integer, primary_key=True, nullable=False)
    start_date      = Column(Date, nullable=False)
    end_date        = Column(Date)
    cell_id         = Column(Integer, ForeignKey("cell.id"), nullable=False)
    citizen_id      = Column(Integer, ForeignKey("citizen.id"), nullable=False)



    def __repr__(self):
        return "<Arrest: id = %d  start_date = %s  closed_date = %s  cell_id = %d citizen_id = %>" % (
            self.id, self.start_date, self.end_date, self.cell_id, self.citizen_id
        )