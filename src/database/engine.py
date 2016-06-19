from sqlalchemy import create_engine


class EngineAlreadyCreatedException(Exception):
    pass


class DBEngine:
    engine = None

    def __init__(self, config):

        if DBEngine.engine:
            raise EngineAlreadyCreatedException

        self.config = config
        self.create()

    def create(self):
        DBEngine.engine = create_engine('postgresql://%s:%s@%s:%d/%s'
                                        % (self.config.user, self.config.password,
                                           self.config.host, self.config.port,
                                           self.config.database))
    @staticmethod
    def get_engine():
        return DBEngine.engine

    @staticmethod
    def reset():
        DBEngine.engine = None
