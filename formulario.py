from wtforms import Form
from wtforms import StringField, TextField, SelectField, IntegerField
from wtforms import validators
from wtforms.fields.html5 import EmailField, DateField
from wtforms.fields import TextAreaField

class Datos(Form):
    nom_solicitante = StringField('Nombre y Apellidos',
    [
        validators.length(min=3, max=40, message='ingrese un nombre valido'),
        validators.Required(message='Este dato es necesario')
    ])
    ciudad = StringField('Ciudad',
    [
        validators.length(min=3, max=15, message='ingrese una ciudad válida'),
        validators.Required(message='Este dato es necesario')
    ])
    condi_solici = SelectField(r'Condición', choices=[('tercero', 'Tercero'), ('familiar', 'Familiar'), ('apoderado', 'Apoderado'), ('afectado', 'Afectado')])


    direccion_solicitante = StringField('Dirección del solicitante',
    [
        validators.Required(message='este dato es necesario')
    ])
    ced_solicitante = StringField('Número de documento de identidad solicitante',
    [
        validators.length(min=6, max=15, message='ingrese un número de identidad valido'),
        validators.Required(message='este dato es necesario')
    ])
    email_solicitante = EmailField('Correo electrónico solicitante')

    num_solicitante = StringField('Número de teléfono solicitante',
    [
        validators.length(min=7, max=12, message='ingrese un número de teléfono válido'),
        validators.Required(message='este dato es necesario')
    ])


    #AFECTADO
    nom_afectado = StringField('Nombre y apellidos del afectado',
    [
        validators.Required(message='este dato es necesario')
    ])
    nom_autoridad = StringField('Autoridad que hizo la detención')
    fecha_hechos = DateField('Fecha', format='%Y-%m-%d')

    sujeto_ordeno = StringField('Persona que ordenó la detención')
    cargo_txt = StringField('Cargo de quien ordenó la detención')

    num_dias = IntegerField('Número de días desde la detención')

    sitio = StringField('Lugar de reclusión')

    ced_afectado = StringField('Número de documento de identidad del afectado',
    [
        validators.length(min=6, max=15, message='ingrese un número de identidad valido'),
        validators.Optional()
    ])
    gen_afectado = SelectField(r'Género afectado', choices=[('m', 'Masculino'), ('f', 'Femenino'), ('o', 'Otro')])

    #HECHOS
    hechos = TextAreaField('Relación de hechos adicionales')
