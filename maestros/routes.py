from . import maestros
import forms
from flask import redirect, render_template, request, url_for
from models import Maestros, db


@maestros.route("/maestros", methods=["GET", "POST"])
@maestros.route("/index")
def index():
    lista = Maestros.query.all()
    return render_template("maestros/listadoMaes.html", maestros=lista)


@maestros.route("/nuevoMaestro", methods=["GET", "POST"])
def nuevo_maestro():
    create_form = forms.MaestroForm()
    if create_form.validate_on_submit():
        maestro = Maestros(
            nombre=create_form.nombre.data,
            apellidos=create_form.apellidos.data,
            especialidad=create_form.especialidad.data,
            email=create_form.email.data,
        )
        db.session.add(maestro)
        db.session.commit()
        return redirect(url_for('maestros.index'))
    return render_template("maestros/nuevoMaestro.html", form=create_form)


@maestros.route("/modificarMaestro", methods=["GET", "POST"])
def modificar_maestro():
    create_form = forms.MaestroForm()

    if request.method == 'GET':
        id = request.args.get('matricula')
        maestro = db.session.query(Maestros).filter(Maestros.matricula == id).first()
        create_form.nombre.data = maestro.nombre
        create_form.apellidos.data = maestro.apellidos
        create_form.especialidad.data = maestro.especialidad
        create_form.email.data = maestro.email
        return render_template("maestros/modificarMaestro.html", form=create_form, id=id)

    if request.method == 'POST':
        id = request.form.get('matricula')
        maestro = db.session.query(Maestros).filter(Maestros.matricula == id).first()
        maestro.nombre = create_form.nombre.data
        maestro.apellidos = create_form.apellidos.data
        maestro.especialidad = create_form.especialidad.data
        maestro.email = create_form.email.data
        db.session.commit()
        return redirect(url_for('maestros.index'))


@maestros.route("/detallesMaestro", methods=["GET"])
def detalles_maestros():
    matricula = request.args.get('matricula')
    maestro = db.session.query(Maestros).filter(Maestros.matricula == matricula).first()
    return render_template(
        'maestros/detallesMaestro.html',
        id=maestro.matricula,
        nombre=maestro.nombre,
        apellidos=maestro.apellidos,
        especialidad=maestro.especialidad,
        email=maestro.email
    )

@maestros.route("/maestros/eliminar", methods=["GET", "POST"])
def eliminar():
    create_form = forms.MaestroForm(request.form)
 
    if request.method == 'GET':
        matricula = request.args.get('matricula')
        if matricula:
            maestro = db.session.query(Maestros).filter(Maestros.matricula == matricula).first()
            if maestro:
                create_form.matricula.data = maestro.matricula
                create_form.nombre.data = maestro.nombre
                create_form.apellidos.data = maestro.apellidos
                create_form.especialidad.data = maestro.especialidad
                create_form.email.data = maestro.email
 
    if request.method == "POST" and create_form.validate():
        matricula = create_form.matricula.data
        maestro = db.session.query(Maestros).filter(Maestros.matricula == matricula).first()
        if maestro:
            db.session.delete(maestro)
            db.session.commit()
            return redirect(url_for('maestros.index'))
    return render_template('maestros/eliminar.html', form=create_form)

@maestros.route('/perfil/<nombre>')
def perfil(nombre):
    return f"Perfil de {nombre}"