#Import para la funcion de calcular
from math import sqrt

apartas=[]
archi=open('Apartas.txt','a+')
archi.close()

def grabar(hecho):
        archi=open('Apartas.txt','a')
        archi.write(hecho+"\n")
        archi.close()
        
def leertxt():
    global apartas
    archi=open('Apartas.txt','r')
    linea=archi.readline()
    #print(linea)
    while linea!="":
        lista=linea.split(";")
        lista[-1] = lista[-1][:-1]
        apartas.append(lista)
        #print(apartas)
        linea=archi.readline()
    archi.close()

def eliminarTxt():
    f = open("Apartas.txt","r")
    lineas = f.readlines()
    f.close()
    f = open("Apartas.txt","w")
    for linea in lineas:
        if linea!="":
            f.write("\n")
    f.close()

def getAparta(titulo):
    global apartas
    for each in apartas:
    	if each[0] == titulo:
    		return each

def getTodosApartas():
    global apartas
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

def cercania(lista):
    latTec=9.8539039
    longTec=-83.9095341
    for each in lista:
            form=sqrt(((-83.9095341-float(each[11]))**2)+((9.8539039-float(each[10]))**2))                
            each[10]=form
    lista.sort(key=lambda pos:pos[10])
    return lista

def ordenaApartas(paraOrdenar,num):
    temp=[]
    if num==0:
        return paraOrdenar
    elif num==1:
        paraOrdenar.sort(key=lambda pos: int(pos[12]))
        return paraOrdenar
    elif num==2:
##            lat [10]   y   long [11]
        return cercania(paraOrdenar)
        
##Las posiciones para esta funcion son: TV,luz,agua,internet,num_cuartos,cochera,ubicacion,precio
def consultarAparta(TV,luz,agua,internet,num_cuartos,cochera,alimentacion,amueblado,precio_min,precio_max,num): #self,
        #self.TV=TV
        #self.luz=luz
        #self.agua=agua
        #self.internet=internet
        #self.num_cuartos=num_cuartos
        #self.cochera=cochera
        #self.alimentacion=alimentacion
        #self.amueblado=amueblado
        #self.num=num
    listaOrden=[]
    global apartas
    listaActual=[TV,luz,agua,internet,cochera,alimentacion,amueblado,num_cuartos,precio_min,precio_max]
    #print "listaActual: ",listaActual
    for each in apartas:
        #print "each: ",each
        if ((listaActual[0]=="True" and each[2]=="True") or (listaActual[0]=="False")) and ((listaActual[1]=="True" and each[3]=="True") or (listaActual[1]=="False")) and ((listaActual[2]=="True" and each[4]=="True") or (listaActual[2]=="False")) and ((listaActual[3]=="True" and each[5]=="True") or (listaActual[3]=="False")) and ((listaActual[4]=="True" and each[7]=="True") or (listaActual[4]=="False")) and ((listaActual[5]=="True" and each[8]=="True")or(listaActual[5]=="False")) and ((listaActual[6]=="True" and each[9]=="True") or (listaActual[6]=="False"))and(listaActual[7]==each[6])and(int(listaActual[8])<=int(each[12])<=int(listaActual[9])):
            listaOrden += [each]
    return ordenaApartas(listaOrden,num)

## Clase Apartamento 
class Residencia(object):
    global apartas
    def __init__(self,titulo,descripcion,TV,luz,agua,internet,num_cuartos,cochera,alimentacion,amueblado,latitud,longitud,precio,correo,telefono):

            if type(self) is Residencia:
                raise Exception('Error: Acceso denegado')
            else:         

                self.publicarAparta(titulo,descripcion,TV,luz,agua,internet,num_cuartos,cochera,alimentacion,amueblado,latitud,longitud,precio,correo,telefono)
    ##Consiste en la funcion que publica Apartamentos, Casas y Habitaciones para el alquiler.
    def publicarAparta(self,titulo,descripcion,TV,luz,agua,internet,num_cuartos,cochera,alimentacion,amueblado,latitud,longitud,precio,correo,telefono):
            
                self.titulo=titulo
                self.descripcion=descripcion
                self.TV=TV
                self.luz=luz
                self.agua=agua
                self.internet=internet
                self.num_cuartos=num_cuartos
                self.cochera=cochera
                self.latitud=latitud
                self.longitud=longitud
                self.precio=precio
                self.correo=correo
                self.telefono=telefono
                self.alimentacion=alimentacion
                self.amueblado=amueblado        
                global apartas
                paraGrabar=''
                if self.verificarAparta(titulo)==False and telefono.isdigit() and precio.isdigit():
                    paraGrabar=self.titulo+';'+self.descripcion+';'+str(self.TV)+';'+str(self.luz)+';'+str(self.agua)+';'+str(self.internet)+';'+str(self.num_cuartos)+';'+str(self.cochera)+';'+str(self.alimentacion)+';'+str(self.amueblado)+';'+str(self.latitud)+';'+str(self.longitud)+';'+str(self.precio)+';'+str(self.correo)+';'+str(self.telefono)
                    grabar(paraGrabar)
                    paraGrabar=paraGrabar.split(';')
                    apartas.append(paraGrabar)            
                                
                else:
                    return "Error: Datos invalidos o apartamento existente."

    ##Retorna True si la residencia que se desea ingresar ya existe.    
    def verificarAparta(self,titulo):
        self.titulo=titulo
        global apartas
        contAp=0
        while contAp<len(apartas):
            if apartas[contAp][0]==self.titulo:
                return True
            else:
                contAp+=1
        return False



class Casa(Residencia):
    def __init__(self,titulo,descripcion,TV,luz,agua,internet,num_cuartos,cochera,alimentacion,amueblado,latitud,longitud,precio,correo,telefono):
        Residencia.__init__(self,titulo,descripcion+'. Casa de habitacion.',TV,luz,agua,internet,num_cuartos,cochera,alimentacion,amueblado,latitud,longitud,precio,correo,telefono)
class Habitacion(Residencia):
    def __init__(self,titulo,descripcion,TV,luz,agua,internet,num_cuartos,cochera,alimentacion,amueblado,latitud,longitud,precio,correo,telefono):
        Residencia.__init__(self,titulo,descripcion+'. Habitacion',TV,luz,agua,internet,'1',cochera,alimentacion,amueblado,latitud,longitud,precio,correo,telefono)

class Apartamento(Residencia):
    def __init__(self,titulo,descripcion,TV,luz,agua,internet,num_cuartos,cochera,alimentacion,amueblado,latitud,longitud,precio,correo,telefono):
        Residencia.__init__(self,titulo,descripcion+'. Apartamento.',TV,luz,agua,internet,num_cuartos,cochera,alimentacion,amueblado,latitud,longitud,precio,correo,telefono)

leertxt()


