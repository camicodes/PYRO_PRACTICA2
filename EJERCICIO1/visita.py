
# Este es el codigo para las visitas al almacen.
from mailbox import NoSuchMailboxError
from pickle import FALSE
import sys
import Pyro4
import Pyro4.util
from almacen import Almacen
from persona import Persona

#Pyro4.util.excepthook como excepthook. esto hace con las excepciones 
# y los stack traces que produce tu programa cuando algo va mal con un objeto Pyro.
sys.excepthook = Pyro4.util.excepthook

#servidor de nombres: pedirle a Pyro que localice el objeto almacén automáticamente
almacen = Pyro4.Proxy("PYRONAME:ejemplo.almacen")

#Solicitar el nombre del visitante en el menu
persona = input("Ingrese su nombre por favor: ")

#Crear un metodo donde solicita el nombre en el menu
def solicitar_nombre():
    return persona

#Instanciar la clase Almacen
almacen=Almacen()

#Creacion del menu de visita
while True:
    print ("")
    print ("-------Bazar Clarita------------")
    print ("Digite la opción deseada: ")
    print ("1.-Listar Productos ")
    print ("2.-Agregar un producto")
    print ("3.-Comprar un producto")
    print ("4.-Salir")
    opcion = input ("Digite la opción:")
    if opcion == '4':
        break
    if opcion =='1':
        nombre = Persona(solicitar_nombre())
        nombre.visita(almacen)
    if opcion =='2':
        nombre = Persona(solicitar_nombre())
        nombre.almacenar(almacen)
    if opcion =='3':
        nombre = Persona(solicitar_nombre())
        nombre.comprar(almacen)




