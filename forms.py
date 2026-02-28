from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from wtforms.fields import EmailField
from wtforms.validators import DataRequired, Length, Email, NumberRange

class UsuarioForm(FlaskForm):
    
    id = IntegerField(
        'ID',
        validators=[
            NumberRange(min=1, max=20, message='Valor no válido')
        ]
    )
    
    nombre = StringField(
        'Nombre',
        validators=[
            DataRequired(message='El nombre es requerido'),
            Length(min=4, max=20, message='Debe tener entre 4 y 20 caracteres')
        ]
    )

    apellidos = StringField(
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
    
    telefono = StringField(
        'Telefono',
        validators=[
            DataRequired(message='El Telefono es requerido'),
        ]
    )