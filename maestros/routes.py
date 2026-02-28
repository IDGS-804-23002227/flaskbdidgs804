from . import maestros
import forms
from flask import render_template, request
from models import Maestros
 
 
@maestros.route("/maestros", methods=["GET", "POST"])
@maestros.route("/index")
def index():
    create_form=forms.UsuarioForm(request.form)
    maestros=Maestros.query.all()
    return render_template("maestros/listradoMaes.html",form=create_form,maestros=maestros)

@maestros.route('/perfil/<nombsre>')
def perfil(nombre):
    return f"Perfil de {nombre}"



