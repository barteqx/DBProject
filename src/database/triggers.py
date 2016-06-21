__author__ = 'bartoszzasieczny'


class DBTriggers:

    def __init__(self, engine):
        self.engine = engine
        self.triggers = []

    def create_triggers(self):
        for trigger in self.triggers:
            self.engine.execute(trigger)