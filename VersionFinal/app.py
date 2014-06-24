'''________________________________________________________________________
					
					Instituto Tecnologico de Costa Rica
					     Lenguajes de Programacion	
					     Segunda Tarea Programada 
					     App Web en Python
					
					Realizado por: 
					        * Josue Espinoza Castro 
						* Mauricio Gamboa Cubero
						* Andres Pacheco Quesada

					Junio del 2014
__________________________________________________________________________'''

#Imports del framework para la aplicacion web: Flask
from flask import Flask
from flask import request, redirect, url_for, abort, session, render_template, jsonify

#Import del modulo de apartamento
import Apartamentos

#Import del modulo de usuarios
import Usuario

#Import para validar info obtenida de forms
import unicodedata

#Nombre de la aplicacion: Bumbur
app = Flask("Apartas")

#----------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------	FRONTEND           ------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------------

#Variable global del usuario en uso actualmente
prueba = []
prueba2 = ""

#URL y funcion para home
@app.route('/')
def home():
	return render_template('home.html')

#URL y funcion para la pagina de buscar apartamentos
@app.route('/buscar')
def buscar():
	return render_template('buscar.html')
	
#URL y funcion para la pagina de apartamentos favoritos
@app.route('/favoritos')
def favoritos():
	global prueba
	lista = Usuario.MostrarFavoritos(prueba[1])
	lista = cambiarAparta(lista)
	return render_template('favoritos.html',lista=lista) 
	
#URL y funcion para la pagina de solicitar un aparta
@app.route('/preguntarAparta', methods=['POST'])
def preguntarAparta():
	lista = Apartamentos.getTodosApartas()
	return render_template('preguntarAparta.html',lista=lista)
	
@app.route('/agregarFavoritos', methods=['POST'])
def agregarFavoritos():
	aparta1 = Apartamentos.getAparta(unicodedata.normalize('NFKD', request.form.getlist('selection')[0]).encode('ascii','ignore'))
	global prueba
	Usuario.Favoritos(prueba[1],aparta1)
	return render_template('felicidades2.html',mensaje=["Agregado a favoritos!"])

#URL y funcion para la pagina de mostrar un aparta
@app.route('/mostrarAparta', methods=['POST'])
def mostrarAparta():
	aparta1 = Apartamentos.getAparta(unicodedata.normalize('NFKD', request.form.getlist('selection2')[0]).encode('ascii','ignore'))
	aparta1 = cambiarAparta2(aparta1)
	return render_template('MostrarAparta.html',lista=[aparta1],lat=aparta1[-2],lng=aparta1[-1])
    
#URL y funcion para la pagina de ingresar un nuevo apartamento
@app.route('/ingresar')
def ingresar():
	return render_template('ingresar.html')

#URL y funcion para el ingreso de un usuario existente
@app.route('/ingreso', methods=['POST'])
def ingreso():
    Contrasena = unicodedata.normalize('NFKD', request.form['Contrasena2']).encode('ascii','ignore')
    Email = unicodedata.normalize('NFKD', request.form['Email2']).encode('ascii','ignore')

    if Usuario.ingreso(Email,Contrasena):
    	global prueba
    	prueba = Usuario.getUsuario(Email)
    	#print "Prueba: ",prueba
    	return render_template('home2.html')
    else:
	return render_template('error.html',mensaje=["Usuario no registrado o credenciales no concordantes."])

#URL y funcion para el menu de inicio
@app.route('/home2')
def home2():
    return render_template('home2.html')

#URL y funcion para la pagina de ingresar un nuevo usuario 
@app.route('/newUsuario', methods=['POST'])
def newUsuario():
    Email = unicodedata.normalize('NFKD', request.form['Email']).encode('ascii','ignore')
    Contrasena = unicodedata.normalize('NFKD', request.form['Contrasena']).encode('ascii','ignore')
    Nombre = unicodedata.normalize('NFKD', request.form['Nombre']).encode('ascii','ignore')
    Telefono = unicodedata.normalize('NFKD', request.form['Telefono']).encode('ascii','ignore')
    
    prueba = Usuario.Usuario(Nombre,Email,Contrasena,Telefono)
    prueba2 = Usuario.Usuario(Nombre,Email,Contrasena,Telefono)

    if Telefono.isdigit():
	if Usuario.VerificarRegistrado(Email):
        	return render_template('error.html',mensaje=["Usuario ya registrado."])
	elif prueba.NuevoUsuario():
		return render_template('felicidades.html',mensaje=["Usuario creado con exito. Ahora, realice el Log In."])
	else:
        	return render_template('error.html',mensaje=["Usuario no existente en Facebook. Revise su correo y contrasena."])	
    else:
        return render_template('error.html',mensaje=["Debe ingresar un numero en el espacio de telefono."])

#URL y funcion para la pagina para mostrar todos los apartas
@app.route('/mostrarTodos', methods=['POST'])
def mostrarTodos():
    lista = Apartamentos.getTodosApartas()
    return render_template('mostrarResultado.html',lista=lista)

#URL y funcion para la pagina de ingresar un nuevo usuario 
@app.route('/newAparta', methods=['POST'])
def newAparta():

    Titulo = unicodedata.normalize('NFKD', request.form['Titulo']).encode('ascii','ignore')
    Descripcion = unicodedata.normalize('NFKD', request.form['Descripcion']).encode('ascii','ignore')
    Descripcion = Descripcion.replace("\t","",Descripcion.count("\t"))
    Descripcion = Descripcion.replace("\n"," ",Descripcion.count("\n"))
    Descripcion = Descripcion.replace("\r"," ",Descripcion.count("\r"))
    Tipo = unicodedata.normalize('NFKD', request.form.getlist('selection')[0]).encode('ascii','ignore')

    try: 
	cochera = unicodedata.normalize('NFKD', request.form.getlist('cochera')[0]).encode('ascii','ignore')
	cochera = True
    except: cochera = False
    
    try: 
	luz = unicodedata.normalize('NFKD', request.form.getlist('luz')[0]).encode('ascii','ignore')
        luz = True
    except: luz = False

    try: 
	agua = unicodedata.normalize('NFKD', request.form.getlist('agua')[0]).encode('ascii','ignore')
	agua = True
    except: agua = False

    try: 
	amueblado = unicodedata.normalize('NFKD', request.form.getlist('amueblado')[0]).encode('ascii','ignore')
	amueblado = True
    except: amueblado = False

    try: 
	alimentacion = unicodedata.normalize('NFKD', request.form.getlist('alimentacion')[0]).encode('ascii','ignore')
	alimentacion = True
    except: alimentacion = False

    try: 
	cable = unicodedata.normalize('NFKD', request.form.getlist('cable')[0]).encode('ascii','ignore')
	cable = True
    except: cable = False

    try: 
	internet = unicodedata.normalize('NFKD', request.form.getlist('internet')[0]).encode('ascii','ignore')
	internet = True
    except: internet = False

    
    Cuartos = unicodedata.normalize('NFKD', request.form.getlist('selection2')[0]).encode('ascii','ignore')
    Precio = unicodedata.normalize('NFKD', request.form['Precio']).encode('ascii','ignore')
    
    try: 
    	 Precio = int(Precio)
    	 Precio = str(Precio)
    except: 
    	 return render_template('error.html',mensaje=["Precio debe ser un numero."])
    	 
    Latitud = unicodedata.normalize('NFKD', request.form['lat']).encode('ascii','ignore')
    Longitud = unicodedata.normalize('NFKD', request.form['lng']).encode('ascii','ignore')
    
    global prueba
    print "Prueba: ",prueba
    
    if Tipo == "Apartamento":
    	 p = Apartamentos.Apartamento(Titulo,Descripcion,cable,luz,agua,internet,Cuartos,cochera,alimentacion,amueblado,Latitud,Longitud,Precio,prueba[1],prueba[2])
    elif Tipo == "Casa":
    	p = Apartamentos.Casa(Titulo,Descripcion,cable,luz,agua,internet,Cuartos,cochera,alimentacion,amueblado,Latitud,Longitud,Precio,prueba[1],prueba[2])
    else: #es una habitacion
    	p = Apartamentos.Habitacion(Titulo,Descripcion,cable,luz,agua,internet,Cuartos,cochera,alimentacion,amueblado,Latitud,Longitud,Precio,prueba[1],prueba[2])
    
    return render_template('felicidades2.html',mensaje=["Aparta ingresado con exito."])
    
#URL y funcion para la pagina de buscar apartas
@app.route('/buscarAparta', methods=['POST'])
def buscarAparta():

    try: 
	cochera = unicodedata.normalize('NFKD', request.form.getlist('cochera')[0]).encode('ascii','ignore')
	cochera = "True"
    except: cochera = "False"
    
    try: 
	luz = unicodedata.normalize('NFKD', request.form.getlist('luz')[0]).encode('ascii','ignore')
        luz = "True"
    except: luz = "False"

    try: 
	agua = unicodedata.normalize('NFKD', request.form.getlist('agua')[0]).encode('ascii','ignore')
	agua = "True"
    except: agua = "False"

    try: 
	amueblado = unicodedata.normalize('NFKD', request.form.getlist('amueblado')[0]).encode('ascii','ignore')
	amueblado = "True"
    except: amueblado = "False"

    try: 
	alimentacion = unicodedata.normalize('NFKD', request.form.getlist('alimentacion')[0]).encode('ascii','ignore')
	alimentacion = "True"
    except: alimentacion = "False"

    try: 
	cable = unicodedata.normalize('NFKD', request.form.getlist('cable')[0]).encode('ascii','ignore')
	cable = "True"
    except: cable = "False"

    try: 
	internet = unicodedata.normalize('NFKD', request.form.getlist('internet')[0]).encode('ascii','ignore')
	internet = "True"
    except: internet = "False"

    Cuartos = unicodedata.normalize('NFKD', request.form.getlist('selection2')[0]).encode('ascii','ignore')
    PrecioMinimo = unicodedata.normalize('NFKD', request.form['PrecioMinimo']).encode('ascii','ignore')
    PrecioMaximo = unicodedata.normalize('NFKD', request.form['PrecioMaximo']).encode('ascii','ignore')
    try:
    	 Ordenamiento = unicodedata.normalize('NFKD', request.form.getlist('ordenamiento')[0]).encode('ascii','ignore')
    	 Ordenamiento = int(Ordenamiento)
    except: Ordenamiento = 0
    
    try: 
    	 PrecioMinimo = int(PrecioMinimo)
         PrecioMinimo = str(PrecioMinimo)
         PrecioMaximo = int(PrecioMaximo)
         PrecioMaximo = str(PrecioMaximo)
    except: 
    	 return render_template('error.html',mensaje=["Precios deben ser numeros."])

#(Titulo,Descripcion,cable,luz,agua,internet,Cuartos,cochera,alimentacion,amueblado,Latitud,Longitud,Precio,prueba[1],prueba[2])

    #print "Datos: ",cable,luz,agua,internet,Cuartos,cochera,alimentacion,amueblado,PrecioMinimo,PrecioMaximo,Ordenamiento

    if int(PrecioMinimo) < int(PrecioMaximo):
    	 lista = Apartamentos.consultarAparta(cable,luz,agua,internet,Cuartos,cochera,alimentacion,amueblado,PrecioMinimo,PrecioMaximo,Ordenamiento)
    	 nuevaLista = []
    	 #print lista
    	 for each in lista:
    	 	print each
    	 	aparta = []
    	 	aparta+=[each[0]]
    	 	aparta+=[each[1]]
    	 	facilidades = ""
    	 	if each[2] == 'True':
    	 		facilidades += "TV Cable, "
    	 	if each[3] == 'True':
    	 		facilidades += "Luz, "
    	 	if each[4] == 'True':
    	 		facilidades += "Agua Caliente, "
    	 	if each[5] == 'True':
    	 		facilidades += "Internet, "
    	 	if each[7] == 'True':
    	 		facilidades += "Cochera, "
    	 	if each[8] == 'True':
    	 		facilidades += "Alimentacion, "
    	 	if each[9] == 'True':
    	 		facilidades += "Amueblado, "
    	 	aparta+=[facilidades]
    	 	aparta+=[each[6]]
    	 	aparta+=[each[12]]
    	 	aparta+=[each[13]]
    	 	aparta+=[each[14]]
    	 	nuevaLista+=[aparta]
	 return render_template('mostrarResultado.html',lista=nuevaLista)
    else:
    	 return render_template('error.html',mensaje=['El precio minimo debe ser menor que el precio maximo'])


#----------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------		BACKEND         ---------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------------

#Para que se muestre en pantalla solo lo necesario
def cambiarAparta(apartas):
    nuevaLista = []
    for each in apartas:
    	 #print each
    	 aparta = []
    	 aparta+=[each[0]]
    	 aparta+=[each[1]]
    	 facilidades = ""
    	 if each[2] == 'True':
    	 	facilidades += "TV Cable, "
    	 if each[3] == 'True':
    	 	facilidades += "Luz, "
    	 if each[4] == 'True':
    	 	facilidades += "Agua Caliente, "
    	 if each[5] == 'True':
    	 	facilidades += "Internet, "
    	 if each[7] == 'True':
    	 	facilidades += "Cochera, "
    	 if each[8] == 'True':
    	 	facilidades += "Alimentacion, "
    	 if each[9] == 'True':
    	 	facilidades += "Amueblado, "
    	 aparta+=[facilidades]
    	 aparta+=[each[6]]
    	 aparta+=[each[12]]
    	 aparta+=[each[13]]
    	 aparta+=[each[14]]
    	 nuevaLista+=[aparta]
    return nuevaLista
    
#Para que se muestre en pantalla solo lo necesario
def cambiarAparta2(aparta):
    print aparta
    nuevaLista = []
    nuevaLista+=[aparta[0]]
    nuevaLista+=[aparta[1]]
    facilidades = ""
    if aparta[2] == 'True':
    	facilidades += "TV Cable, "
    if aparta[3] == 'True':
    	facilidades += "Luz, "
    if aparta[4] == 'True':
    	facilidades += "Agua Caliente, "
    if aparta[5] == 'True':
    	facilidades += "Internet, "
    if aparta[7] == 'True':
    	facilidades += "Cochera, "
    if aparta[8] == 'True':
    	facilidades += "Alimentacion, "
    if aparta[9] == 'True':
    	facilidades += "Amueblado, "
    nuevaLista+=[facilidades]
    nuevaLista+=[aparta[6]]
    nuevaLista+=[aparta[12]]
    nuevaLista+=[aparta[13]]
    nuevaLista+=[aparta[14]]
    nuevaLista+=[aparta[10]]
    nuevaLista+=[aparta[11]]
    print nuevaLista
    return nuevaLista
    
#----------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------- 		  MAIN		    -----------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------------

#main de la aplicacion
if __name__ == '__main__':
	app.debug = True
	app.run(host='192.168.0.8')#CAMBIAR ESTE IP POR EL ACTUAL
