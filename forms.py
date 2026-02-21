from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.fields import EmailField
from wtforms.validators import DataRequired, Length, Email

class UsuarioForm(FlaskForm):

    nombre = StringField(
        'Nombre',
        validators=[
            DataRequired(message='El nombre es requerido'),
            Length(min=4, max=20, message='Debe tener entre 4 y 20 caracteres')
        ]
    )

    apaterno = StringField(
        'Apellido',
        validators=[
            DataRequired(message='El apellido es requerido')
        ]
    )

    email = EmailField(
        'Correo',
        validators=[
            DataRequired(message='El correo es requerido'),
            Email(message='Ingrese un correo válido')
        ]
    )