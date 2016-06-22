from src.database import *
from src.config import AppConfig
from sqlalchemy.orm import sessionmaker
from datetime import datetime

class DBApplication:

    def __init__(self):
        self.engine = engine.DBEngine(AppConfig, base_model.BaseModel)

    def initialize(self):
        self.engine.create()
        self.engine.create_schema()

    def create_admin(self):
        Session = sessionmaker(bind=engine.DBEngine.get_engine())
        s = Session()
        citizen = models.Citizen(name="Admin", surname="Administrator", birth_date=datetime.now(), pesel=10000000000)
        s.add(citizen)
        s.commit()
        c = s.query(models.Citizen).filter(models.Citizen.pesel == 10000000000)[0]
        user = models.User(email=AppConfig.default_admin_mail, password=AppConfig.default_admin_pass,
                           citizen_id=c.id, role=2)
        s.add(user)
        s.commit()


def main():
    app = DBApplication()
    app.initialize()
    app.create_admin()

if __name__ == '__main__':
    main()
