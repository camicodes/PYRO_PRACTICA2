#Importar la clase sistema
#Importar libreria de Pyro4
import sistema
import Pyro4
#Llama a los metodos de las clases sistema y Bolsa_valores
Bolsa=sistema.Bolsa_valores()
# Iniciar un servidor Pyro para el objeto Bolsa
Pyro4.Daemon.serveSimple({
    Bolsa: 'bolsa',
    #Agregar un puerto para la conexión del localhost
}, host="localhost", port=65487, ns=False, verbose=True)

