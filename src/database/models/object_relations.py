from sqlalchemy import Integer, Column, ForeignKey
from src.database.base_model import BaseModel

class IsWitness(BaseModel):

    __tablename__ = "is_witness"

    id = Column(Integer, primary_key=True)
    citizen_id = Column(Integer, ForeignKey("citizen.id"), nullable=False)
    investigation_id = Column(Integer, ForeignKey("investigation.id"), nullable=False)

    def __repr__(self):
        return "<IsWitness: citizen_id = %d  investigation_id = %d>" % (
            self.citizen_id, self.investigation_id
        )

class IsSuspected(BaseModel):

    __tablename__ = "is_suspected"

    id = Column(Integer, primary_key=True)
    citizen_id = Column(Integer, ForeignKey("citizen.id"), nullable=False)
    investigation_id = Column(Integer, ForeignKey("investigation.id"), nullable=False)

    def __repr__(self):
        return "<IsSuspected: citizen_id = %d  investigation_id = %d>" % (
            self.citizen_id, self.investigation_id
        )