import web
import hashlib
class Login:

    def GET(self):
        if logged():
            render = create_render(session.privilege)
            return '%s' % render.login_double()
        else:
            render = create_render(session.privilege)
            return '%s' % render.login()