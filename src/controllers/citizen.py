__author__ = 'bartoszzasieczny'
from web import form, template, input
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
        render = template.render('src/templates/citizen')
        myform = citizen_form()
        return render.generic(myform)

    def POST(self):
        try:
            get_input = input()
            render = template.render('src/templates/citizen')
            c = models.Citizen(name=get_input['name'],
                               surname=get_input['surname'],
                               birth_date=parser.parse(get_input['birth_date']),
                               pesel=get_input['pesel'])

            ses = sessionmaker(bind=engine.DBEngine.get_engine());
            s = ses();
            s.add(c)
            s.commit()
            c = s.query(models.Citizen).order_by(models.Citizen.id)
            return render.list(c)

        except Exception, e:
            render = template.render('src/templates')
            return render.error(err_msg=e)

class RemoveCitizen:

    def GET(self):
        try:
            get_input = input(_method='get')
            ses = sessionmaker(bind=engine.DBEngine.get_engine());
            s = ses();
            c = s.query(models.Citizen).filter_by(id=int(get_input['id'])).first()
            s.delete(c)
            s.commit()
            c = s.query(models.Citizen).order_by(models.Citizen.id)
            render = template.render('src/templates/citizen')
            return render.list(c)
        except Exception, e:
            render = template.render('src/templates')
            return render.error(err_msg=e)



class EditCitizen:
    def GET(self):
        try:
            render = template.render('src/templates/citizen')
            get_input = input(_method='get')
            ses = sessionmaker(bind=engine.DBEngine.get_engine());
            s = ses()
            c = s.query(models.Citizen).filter_by(id=int(get_input['id'])).first()
            c_form = form.Form(
                form.Textbox('name', value=c.name),
                form.Textbox('surname', value=c.surname),
                form.Textbox('birth_date', value=str(c.birth_date)),
                form.Textbox('pesel', value=str(c.pesel))
            )
            return render.generic(c_form)
        except Exception, e:
            render = template.render('src/templates')
            return render.error(err_msg=e)

    def POST(self):
        myform = citizen_form()
        try:
            render = template.render('src/templates/citizen')
            get_input = input()
            ses = sessionmaker(bind=engine.DBEngine.get_engine());
            s = ses()
            c = s.query(models.Citizen).filter_by(id=int(get_input['id'])).first()
            c.name = get_input['name']
            c.surname = get_input['surname']
            print get_input['birth_date']
            c.birth_date = parser.parse(get_input['birth_date'])
            c.pesel = int(get_input['pesel'])
            s.commit()
            c = s.query(models.Citizen).order_by(models.Citizen.id)
            return render.list(c)

        except Exception, e:
            render = template.render('src/templates')
            return render.error(err_msg=e)

class ListCitizens:
    def GET(self):
        ses = sessionmaker(bind=engine.DBEngine.get_engine());
        s = ses();
        c = s.query(models.Citizen).order_by(models.Citizen.id)
        render = template.render('src/templates/citizen')
        print render.__dict__
        return render.list(c)