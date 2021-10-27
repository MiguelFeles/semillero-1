from flask import Flask, render_template,  request, make_response, send_file, send_from_directory, abort
from fpdf import FPDF, HTMLMixin #para el pdf
from peticion import generadorPeticion
from datetime import date

app = Flask(__name__)
#pdf = FPDF('P', 'mm', 'letter') #

# @app.route('/')
# def index():
#     title = 'HC4A - Codext'
#     return render_template("index.html", title=title)


@app.route('/about')
def about():
    names = ['Peter','Emma','Juan','Chipss']
    return render_template("about.html", names=names)

@app.route('/about_poder')
def about_poder():
    return render_template("about_poder.html")

@app.route('/')
def inicio():
    return render_template("inicio.html")

@app.route('/habeas', methods=['GET', 'POST'])  #ruta inicial y el metodo post es una forma de recibir la información
def casa():
    #datoshabeas = formulario.Datos(request.form)
    #if request.method == 'POST' and datoshabeas.validate():


    return render_template('habeas.html')

@app.route('/form_habeas', methods=['POST'])
def form():

    


    return render_template("form.html", id_solicitante=id_solicitante, id_afectado=id_afectado, fecha= fecha, title = title, texto=texto, nom_solicitante = nom_solicitante, ciudad = ciudad, condi_solici = condi_solici, direccion_solicitante = direccion_solicitante , email_solicitante = email_solicitante, ced_solicitante = ced_solicitante, num_solicitante = num_solicitante, nom_afectado = nom_afectado, nom_autoridad = nom_autoridad, fecha_hechos = fecha_hechos, sujeto_ordeno = sujeto_ordeno, cargo_txt = cargo_txt, ced_afectado = ced_afectado, num_dias = num_dias, gen_afectado = gen_afectado, sitio = sitio , hechos = hechos)#, datoshabeas=datoshabeas.ciudad.data)

@app.route('/download/<pdf_name>')
def download_file(pdf_name):
    path = r'/static/client/pdf'
    try:
        return send_file(pdf_name, as_attachment=True)
    except FileNotFoundError:
        abort(404, description=path+pdf_name+"Not Found")


#====================================DERECHO DE PETICIÓN========================================
@app.route('/peticion', methods=['GET', 'POST'])

def peticion():
    return render_template('peticion.html')


@app.route('/form_peticion', methods=['POST'])
def form_peticion():
    tuplaPeticion = generadorPeticion()
    nom_peticionario = tuplaPeticion[0]
    ced_peticionario = tuplaPeticion[1]
    derechoPeticion = tuplaPeticion[2]

    return render_template('form_peticion.html', nom_peticionario = nom_peticionario, ced_peticionario = ced_peticionario, derechoPeticion = derechoPeticion)



#=====================================PODER AUTOMATIZADO========================================
@app.route('/poder', methods=['GET', 'POST'])  #ruta inicial y el metodo post es una forma de recibir la información
def poder():
    return render_template('poder.html')




@app.route('/form_poder',methods=['POST'])
def form_poder():
    

    return  render_template("form_poder.html",
    nom_poder=nom_poder,
    gen_poder=gen_poder,
    id_poder = id_poder,
    ced_poder = ced_poder,
    email=email,
    nom_apo=nom_apo,
    gen_apo=gen_apo,
    id_apo = id_apo ,
    ced_apo=ced_apo,
    portadore = portadore,
    num_car = num_car,
    email_apo=email_apo,
    tipo_proceso = tipo_proceso,
    nom_contra=nom_contra,
    gen_contra=gen_contra,
    id_contra = id_contra,
    ced_contra=ced_contra,
    email_2=email_2,



    )



if __name__ == '__main__':
    app.run(debug = True)
