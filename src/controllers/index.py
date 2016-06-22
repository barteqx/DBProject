__author__ = 'bartoszzasieczny'

import web
from src.controllers.helpers import *


class Login:

    def GET(self):
        render = web.template.render('templates/')
        if logged():
            return '%s' % render.index()
        else:
            return '%s' % render.landing()
