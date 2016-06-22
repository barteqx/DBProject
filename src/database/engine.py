from sqlalchemy import create_engine
from src.database.triggers import DBTriggers


class EngineAlreadyCreatedException(Exception):
    pass


class DBEngine:
    engine = None

    def __init__(self, config, base_model):
        if DBEngine.engine:
            raise EngineAlreadyCreatedException

        self.config = config
        self.base_model = base_model

    def create(self):
        DBEngine.engine = create_engine('postgresql://%s:%s@%s:%s/%s'
                                        % (self.config.user, self.config.password,
                                           self.config.host, self.config.port,
                                           self.config.database))

    def create_schema(self):
        if self.check_schema():
            return 0

        self.reset_schema()

    def reset_schema(self):
        triggers = DBTriggers(DBEngine.get_engine())

        triggers.drop_triggers()

        self.base_model.metadata.drop_all(DBEngine.get_engine())
        self.base_model.metadata.create_all(DBEngine.get_engine())

        triggers.create_triggers()

    def check_schema(self):

        _tables =  ['arrest',
                   'cell',
                   'citizen',
                   'fine',
                   'investigation',
                   'is_suspected',
                   'is_witness',
                   'policeman',
                   'user'
                   ]

        _query = "SELECT table_name FROM information_schema.tables WHERE table_schema = 'public' ORDER BY table_name;"

        result = [row[0] for row in DBEngine.engine.execute(_query)]

        for table in _tables:
            if table not in result:
                return False

        return True

    @staticmethod
    def get_engine():
        return DBEngine.engine

    @staticmethod
    def reset():
        DBEngine.engine = None
