__author__ = 'bartoszzasieczny'

class DBConstraints:

    def __init__(self, engine):
        self.engine = engine
        self.constraints = [
            """

            """,
            """

            """
        ]

    def create_constraints(self):
        for constraint in self.constraints:
            self.engine.get_engine().execute(constraint)


