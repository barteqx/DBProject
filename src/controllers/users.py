__author__ = 'bartoszzasieczny'
from web import form, template, input
from sqlalchemy.orm import sessionmaker
from dateutil import parser
from src.controllers.helpers import *
from src.database import *

global session

user_form = form.Form(
    form.Textbox('email'),
    form.Textbox('password'),
    form.Textbox('role'),
    form.Textbox('citizen_id'),
)


class CreateUser:

    def GET(self):
        render = template.render('src/templates/user')
        myform = user_form()
        return render.generic(myform)

    def POST(self):
        try:
            get_input = input()
            render = template.render('src/templates/user')
            c = models.User(email=get_input['email'],
                               password=get_input['password'],
                               role=get_input['role'],
                               citizen_id=get_input['citizen_id'])

            ses = sessionmaker(bind=engine.DBEngine.get_engine());
            s = ses();
            s.add(c)
            s.commit()
            c = s.query(models.User).order_by(models.User.id)
            return render.list(c)

        except Exception, e:
            render = template.render('src/templates')
            return render.error(err_msg=e)

class RemoveUser:

    def GET(self):
        try:
            get_input = input(_method='get')
            ses = sessionmaker(bind=engine.DBEngine.get_engine());
            s = ses();
            c = s.query(models.User).filter_by(id=int(get_input['id'])).first()
            s.delete(c)
            s.commit()
            c = s.query(models.User).order_by(models.User.id)
            render = template.render('src/templates/user')
            return render.list(c)
        except Exception, e:
            render = template.render('src/templates')
            return render.error(err_msg=e)



class EditUser:
    def GET(self):
        try:
            render = template.render('src/templates/user')
            get_input = input(_method='get')
            ses = sessionmaker(bind=engine.DBEngine.get_engine());
            s = ses()
            c = s.query(models.User).filter_by(id=int(get_input['id'])).first()
            c_form = form.Form(
                form.Textbox('email', value=c.email),
                form.Textbox('password', value=c.password),
                form.Textbox('role', value=str(c.role)),
                form.Textbox('citizen_id', value=str(c.citizen_id))
            )
            return render.generic(c_form)
        except Exception, e:
            render = template.render('src/templates')
            return render.error(err_msg=e)

    def POST(self):
        try:
            render = template.render('src/templates/user')
            get_input = input()
            ses = sessionmaker(bind=engine.DBEngine.get_engine());
            s = ses()
            c = s.query(models.User).filter_by(id=int(get_input['id'])).first()
            c.email = get_input['email']
            c.password = get_input['password']
            c.role = int(get_input['role'])
            c.citizen_id = int(get_input['citizen_id'])
            s.commit()
            c = s.query(models.User).order_by(models.User.id)
            return render.list(c)

        except Exception, e:
            render = template.render('src/templates')
            return render.error(err_msg=e)

class ListUsers:
    def GET(self):
        ses = sessionmaker(bind=engine.DBEngine.get_engine());
        s = ses();
        c = s.query(models.User).order_by(models.User.id)
        render = template.render('src/templates/user')
        print render.__dict__
        return render.list(c)