__author__ = 'bartoszzasieczny'

import web

class Index:

    def GET(self):
        render = web.template.render('src/templates/')
        return '%s' % render.index()
