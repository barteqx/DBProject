from src.database import *
from src.config import AppConfig

class DBApplication:

    def __init__(self):
        self.engine = engine.DBEngine(AppConfig, base_model.BaseModel)

    def initialize(self):
        self.engine.create()
        self.engine.create_schema()


def main():
    app = DBApplication()
    app.initialize()

if __name__ == '__main__':
    main()
