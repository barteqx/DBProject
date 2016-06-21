__author__ = 'bartoszzasieczny'

import os
import re
import sqlalchemy

class DBTriggers:

    def __init__(self, engine):
        self.engine = engine
        self.triggers = []
        self.delete_triggers = []
        self.load_triggers()

    def load_triggers(self):
        regex = "(.*).sql"
        r = re.compile(regex)
        p = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'triggers')
        walk_res = os.walk(p, topdown=False)

        for _, _, files in walk_res:
            for f in files:
                if not r.match(f):
                    continue
                t = "".join(open(os.path.join(p,f), 'r').readlines())
                self.triggers.append(t)

        self.delete_triggers = open(os.path.join(p, 'triggers_delete'), 'r').readlines()

    def create_triggers(self):
        for trigger in self.triggers:
            self.engine.execute(trigger)

    def drop_triggers(self):
        for command in self.delete_triggers:
            try:
                self.engine.execute(command)
            except sqlalchemy.exc.ProgrammingError:
                pass