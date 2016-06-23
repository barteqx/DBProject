from src.database import *
from src.config import AppConfig
# from src.urls import urls

from sqlalchemy.orm import sessionmaker
from datetime import datetime

# import web
#
# web.config.debug = False
#
# app = web.application(urls, locals())
#
# render = web.template.render('src/templates/')


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
    #app.create_admin()

    #appdb = web.application(urls, globals())
    #store = web.session.DiskStore('sessions')
    #session = web.session.Session(app, store, initializer={'login': 0, 'privilege': 0})
    #appdb.run()

if __name__ == '__main__':
    main()
