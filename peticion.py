from flask import Flask, render_template,  request, make_response, send_file, send_from_directory, abort
from fpdf import FPDF, HTMLMixin #para el pdf
from datetime import date
from fpdf import FPDF, HTMLMixin

def generadorPeticion():

    modHTML = open("./templates/form_peticion.html","w")
    modHTML.write(
    """<!doctype html>
{%extends 'layout.html'%} <!--Para los cambios en el nav bar y etc-->
{%block content%}

<html>
<body>
    <h2>Si todo está en orden, descarga <a href="{{url_for( 'download_file',pdf_name='peticion_'+nom_peticionario[:4]+ced_peticionario[:-3]+'.pdf' ) }}">aquí</a> tu Poder en PDF</h2>""")
    modHTML.close()

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

    

    derechoPeticion = f"""{ciudad_peticion}  {fecha_peticion}<br> 
<br>
Señores.<br>
{dirigido}<br>
{direccion_peticionado}<br>
{email_peticionado}<br>
<br>
Referencia: Derecho de Petición de {nom_peticionario} a {dirigido} para {asunto_peticion}<br>
<br>
{nom_peticionario}, identificad{gen_peticionario} con {id_peticionario} número {ced_peticionario} de {id_expedicion}, en <br>calidad de {id_calidad}; de conformidad con el artículo 23 de la Constitución Política de Colombia de 1991, y del <br>título segundo de la parte primera del Código de Procedimiento Administrativo y de lo Contencioso Administrativo (Ley 1437 de 2011);<br> interpongo el siguiente Derecho de Petición basado en los siguientes:<br>
<br>

I) Hechos.<br>
<br>
{hechos_peticion}<br>
<br>

II) Petición.<br>

En mérito de lo expuesto, se solicita a {dirigido} que:<br>
Petición <br>
{peticionAdd}<br>
<br>
III) Notificaciones.<br>
<br>
Se podrá notificar en cualquiera de las siguientes direcciones.<br>
<br>
{direccion_peticionario}<br>
<br>
{email_peticionario}<br>
<br>
<br>
IV) Firma.<br>
<br>
El presente documento se suscribe de conformidad con el artículo 7 de la Ley 527 de 1999, y con la presunción contemplada <br>en el artículo 244 de la Ley 1564 de 2012 (Código General del Proceso).<br>

<br>

Sin otro particular, <br>

{nom_peticionario}<br>
{id_peticionario} número {ced_peticionario}"""



    class MyFPDF(FPDF, HTMLMixin):
        pass

    pdf = MyFPDF()
    pdf.set_margins(left= 15.0, top=12.5, right=15.0)
    pdf.add_page()
    pdf.write_html(derechoPeticion)
    pdf.output('peticion_'+nom_peticionario[:4]+ced_peticionario[:-3]+'.pdf', 'F')

    
    modHTML = open("./templates/form_peticion.html","a")
    modHTML.write (derechoPeticion)
    modHTML.write("""</body>
    </html>

    {%endblock%}""")
    modHTML.close()

    return(nom_peticionario, ced_peticionario, derechoPeticion)

