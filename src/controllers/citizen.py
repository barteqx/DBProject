__author__ = 'bartoszzasieczny'
from web import form, template
from src.controllers.helpers import *

global session

citizen_form = form.Form(
    form.Textbox('name'),
    form.Textbox('surname'),
    form.Textbox('birth_date'),
    form.Textbox('pesel')
)

render = template.render('templates/')

class CreateCitizen:

    def GET(self):
        myform = citizen_form()
        return render.generic(myform)

    def POST(self):


class RemoveCitizen:

    def GET(self):


class EditCitizen:
    def GET(self):

    def POST(self):


class ListCitizens:
    def GET(self):
