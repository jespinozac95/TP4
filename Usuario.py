import mechanize #Para descargarlo: https://pypi.python.org/pypi/mechanize/


ListaUsuarios=[]
archi=open('Usuarios.txt','a+')
archi.close()




def  grabar(hecho):
    archi=open('Usuarios.txt','a')
    archi.write(hecho+"\n")
    archi.close()

    
def leertxt():
    #ListaUsuarios=Usuario.ListaUsuarios
    global ListaUsuarios 
    archi=open('Usuarios.txt','r')
    linea=archi.readline()
    print(linea)
    while linea!="":
        lista=linea.split(";")
        lista[3]=eval(lista[3])
        ListaUsuarios.append(lista)
        linea=archi.readline()
    archi.close()




def escribir_lista(lista):
    archi=open('Usuarios.txt','a')
    for i in lista:
        contador=0
        while contador<(len(i)-1):
            archi.write(str(i[contador])+";")
            contador+=1
        archi.write(str(i[contador]))
        archi.write("\n")
    archi.close()


def eliminarTxt():
    f = open("Usuarios.txt","r")
    lineas = f.readlines()
    f.close()
    f = open("Usuarios.txt","w")
    for linea in lineas:
        if linea!="":
            f.write("")
    f.close()



#Usuario
class Usuario:
##    ListaUsuarios=[]
##    archi=open('Usuarios.txt','a+')
##    ##archi.write("Hola, no sirvio\n")
##    archi.close()
    global ListaUsuarios

    def __init__(self,nombre,correo,contrasena,telefono):
        
        self.nombre=nombre
        self.__correo=correo
        self.__contrasena=contrasena
        self.telefono=telefono
        self.NuevoUsuario()



    #F: Permite ingresar un  nuevo usuario, verifica el ingreso con Facebook, ademas que este no haya sido registrado anteriormente.
    def NuevoUsuario(self):
        #self.nombre=nombre
        #self.__correo=correo
        #self.__contrasena=contrasena
        #self.telefono=telefono
        #self.favoritos=favoritos
        global ListaUsuarios
        #ListaUsuarios=Usuario.ListaUsuarios
        paraGrabar=''
        #x=Usuario()
        if self.LoginFacebook() and (self.VerificarRegistrado()==False):
              paraGrabar=self.nombre+';'+self.__correo+';'+str(self.telefono)+';'+str([])
              print("Nuevo Usuario TXT: "+paraGrabar)
              grabar(paraGrabar)
              paraGrabar=paraGrabar.split(';')
              paraGrabar[3]=eval(paraGrabar[3])
              ListaUsuarios.append(paraGrabar)        
        else:
             print ("Debe estar registrado en Facebook o su cuenta ha sido creada anteriormente")

             
    #Realiza el Login en Facebook
    def LoginFacebook (self):
         #self.__correo=correo
         #self.__contrasena=contrasena
         
         url="https://www.facebook.com" #Direccion Url a la que se va a ingresar
         fb=mechanize.Browser() 
         fb.set_handle_robots(False) # Se indica que no es un robot
         fb.addheaders=[('User-Agent','Firefox')]
         fb.open(url) #abre la direccion indicada en el url

         #Descomentar para ver el codigo del form
         #for i in fb.forms():
         #     print i
         #https://www.facebook.com/login.php?login_attempt=1

         #<TextControl(email=)>
         #<PasswordControl(pass=)>

         email =self.__correo #Usuario: Correo electronico o numero de telefono
         contrasena =self.__contrasena #Contrasena

         fb.select_form(nr=0)
         fb.form["email"]=email
         fb.form["pass"]=contrasena

         prueba=fb.submit()

         #Descomentar para ver el url que devuelve.
         #print(prueba.geturl())
         if prueba.geturl()!="https://www.facebook.com/login.php?login_attempt=1":
              print ("")
              print ("Facebook login realizado con exito ! \n Usuario:"+email+"\n"+"Contrasena: "+contrasena+"\n")
              return True 
         else:
              print ("Datos incorrectos: revise el correo o la contrasena.")
              return False

    


    #Verifica si el usuario puede ingresar a la aplicacion, suponiendo que este usuario ya se encontraba registrado.      
    def ingreso(self):
         self.correo=correo
         self.contrasena=contrasena
         #x=Usuario()
         if self.LoginFacebook() and self.VerificarRegistrado():
              print ("Bienvenido, ha ingresado correctamente!")
              return True
         else:
              return False
              
    #Verifica si el usuario esta registrado en la aplicacion
    def VerificarRegistrado(self):
         #self.__correo=correo
         global ListaUsuarios
         #ListaUsuarios=Usuario.ListaUsuarios
         print("Lista Usuarios")
         print (ListaUsuarios)
         cont=0
         while cont<len(ListaUsuarios):
              for i in ListaUsuarios:
                   if i[1]==self.__correo:
                        return True
                   else:
                        cont+=1
         return False        

    ##Funcion que recibe el correo del usuario actual (ya que es unico) y el numero identificador del apartamento que desea marcar
    def Favoritos(self,ide): 
        #self.ide=ide
        #self.correo=correo
        
        global ListaUsuarios
        #ListaUsuarios=Usuario.ListaUsuarios
        cont2=0
        while cont2<len(ListaUsuarios):
            if self.__correo==ListaUsuarios[cont2][1]:
                ##ListaUsuarios[cont2][3]=eval(ListaUsuarios[cont2][3])
                ##print(type(ListaUsuarios[cont2][3]))
                ##print(ListaUsuarios[cont2][3])
                if ide not in ListaUsuarios[cont2][3]:
                    temp=ListaUsuarios[cont2][3]
                    ListaUsuarios[cont2][3].append(ide)
                    break
                else:
                    return "errorrrrsh"
            else:
                cont2+=1
        ##print(ListaUsuarios)
        eliminarTxt()
        escribir_lista(ListaUsuarios)
    
                
                

    ##    Funcion que muestra los apartamentos que el usuario marco como favoritos.      
    def MostrarFavoritos(self): 

        #self.correo=correo
        
        global ListaUsuarios
        cont2=0
        while cont2<len(ListaUsuarios):
            if self.__correo==ListaUsuarios[cont2][1]:
                return (ListaUsuarios[cont2][3])
              
            else:
                cont2+=1



leertxt()
#prueba= Usuario("Everardo","everardo@herrera.com","eve",261554)
#prueba.Favoritos("everardo@herrera.com",25)
prueba2= Usuario("Mauricio","mauricio.11.gamboa@gmail.com","bombur123",26155564)
prueba3= Usuario("Andres","andresp11_95@hotmail.com","pequeo",2615864)











