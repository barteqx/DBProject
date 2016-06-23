__author__ = 'bartoszzasieczny'
from web import form, template
from sqlalchemy.orm import sessionmaker
from dateutil import parser
from src.controllers.helpers import *
from src.database import *

global session

citizen_form = form.Form(
    form.Textbox('name'),
    form.Textbox('surname'),
    form.Textbox('birth_date'),
    form.Textbox('pesel')
)


class CreateCitizen:

    def GET(self):

        if logged() and (is_admin() or is_policeman()):
            render = template.render('templates/citizen')
            myform = citizen_form()
            return render.generic(myform)

        else:
            render = template.render('templates/')
            return render.error(err_msg = "You are not logged in.")

    def POST(self):
        myform = citizen_form()
        if logged() and (is_admin() or is_policeman()):
            try:
                render = template.render('templates/citizen')
                c = models.Citizen(name=myform['name'],
                                   surname=myform['surname'],
                                   birthdate=parser.parse(myform['birth_date']),
                                   pesel=myform['pesel'])

                ses = sessionmaker(bind=engine.DBEngine.get_engine());
                s = ses();
                s.add(c)
                s.commit()
                render.list(msg="User created")
            except Exception, e:
                return render.error(err_msg=e)
        else:
            return render.error(err_msg="You are not logged in.")


class RemoveCitizen:

    def GET(self):


class EditCitizen:
    def GET(self):

    def POST(self):


class ListCitizens:
    def GET(self):
