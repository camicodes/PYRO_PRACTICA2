class Persona(object):
    #inicializar los atributos del objeto
    def __init__(self, nombre):
        self.nombre = nombre
    #Se crea un metodo para visitar el almacen
    def visita(self, almacen):
        print("------------------------------------------------------------------------------------")
        print("Hola, {0} .El almacen contiene:".format(self.nombre), almacen.lista_articulos())
        print("------------------------------------------------------------------------------------")
    #Se crea un metodo para almacenar un articulo en la lista
    def almacenar(self, almacen):
        print("El almacen contiene:", almacen.lista_articulos())
        #strip: devuelve una copia de la cadena eliminando los caracteres iniciales y finales
        lista = input("Escriba lo que desea almacenar: ").strip()
        if lista:
            #llama a los articulos del almacen
            almacen.agregar(self.nombre, lista)

    #Se crea un metodo para la compra de articulo
    def comprar(self, almacen):
        print("El almacen contiene:", almacen.lista_articulos())
        #strip: devuelve una copia de la cadena eliminando los caracteres iniciales y finales 
        lista = input("Escriba lo que quiera comprar: ").strip()
        if lista:
            #llama a los articulos del almacen
            almacen.llevar(self.nombre, lista)