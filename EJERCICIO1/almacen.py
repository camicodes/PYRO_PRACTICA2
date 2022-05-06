from persona import Persona
import Pyro4

@Pyro4.expose
@Pyro4.behavior(instance_mode="single")

class Almacen(object):
    #inicializar los atributos del objeto
    def __init__(self):
        self.articulos = ["Cuadernos", "Esferos", "Borradores", "Mochila", "Carpetas"]

    def lista_articulos(self):
        #Imprime la lista de articulos del almacen
        return self.articulos

    def llevar(self, nombre, lista):
        #Se elimina el articulo que fue comprado la lista
        self.articulos.remove(lista)
        print("{0} ha comprado: {1}.".format(nombre, lista))

    def agregar(self, nombre, lista):
        #Agregar un nuevo articulo al final de la lista
        self.articulos.append(lista)
        print("{0} ha agregado: {1}.".format(nombre, lista))

# Iniciar un servidor Pyro para el objeto almacén
def main():
    Pyro4.Daemon.serveSimple(
        {
            Almacen: "ejemplo.almacen"
        },
        ns = True)

if __name__=="__main__":
    main()