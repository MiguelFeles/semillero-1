from flask import Flask, render_template,  request, make_response, send_file, send_from_directory, abort
from fpdf import FPDF, HTMLMixin #para el pdf
from datetime import date

def generadorPeticion():

    peticionAdd = request.form.get('peticiones')
  
    fecha_peticion = request.form.get('fecha_peticion')
    print(fecha_peticion)
    asunto_peticion = request.form.get('asunto_peticion')
    ciudad_peticion = request.form.get('ciudad_peticion')

    nom_peticionario = request.form.get('nom_peticionario').upper()
    
    id_peticionario = request.form.get('id_peticionario')
    ced_peticionario = request.form.get('ced_peticionario').replace('.','').replace(",","")
    id_expedicion = request.form.get('id_expedicion')
    direccion_peticionario = request.form.get('direccion_peticionario') 
    email_peticionario = request.form.get('email_peticionario')

    gen_peticionario = request.form.get('gen_peticionario')
    gen_peticionario = 'o' if gen_peticionario == 'm' else 'a'

    id_calidad = request.form.get('id_calidad')

    representada = request.form.get('representada')
    dirigido = request.form.get('dirigido')

    direccion_peticionado = request.form.get('direccion_peticionado') 
    email_peticionado = request.form.get('email_peticionado')

    hechos_peticion = request.form.get('hechosAdd')

    

    derechoPeticion = f"""{ciudad_peticion}{fecha_peticion}

Señores. 
{dirigido}
{direccion_peticionado}
{email_peticionado}

Referencia: Derecho de Petición de {nom_peticionario} a {dirigido} para {asunto_peticion}

{nom_peticionario}, identificad{gen_peticionario} con {id_peticionario} número {ced_peticionario} de {id_expedicion}, en calidad de {id_calidad}; de conformidad con el artículo 23 de la Constitución Política de Colombia de 1991, y del título segundo de la parte primera del Código de Procedimiento Administrativo y de lo Contencioso Administrativo (Ley 1437 de 2011); interpongo el siguiente Derecho de Petición basado en los siguientes:


I) Hechos.

{hechos_peticion}


II) Petición.

En mérito de lo expuesto, se solicita a {dirigido} que:
Petición 
{peticionAdd}

III) Notificaciones.

Se podrá notificar en cualquiera de las siguientes direcciones.

{direccion_peticionario}

{email_peticionario}


IV) Firma.

El presente documento se suscribe de conformidad con el artículo 7 de la Ley 527 de 1999, y con la presunción contemplada en el artículo 244 de la Ley 1564 de 2012 (Código General del Proceso).



Sin otro particular,



{nom_peticionario}
{id_peticionario} número {ced_peticionario}"""

    
    print("llegué hasta acá")
    return(derechoPeticion)

