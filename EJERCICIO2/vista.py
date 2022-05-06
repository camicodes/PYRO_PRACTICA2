import Pyro4
#Se establece la Uri
s=Pyro4.Proxy("PYRO:bolsa@localhost:65487")
#Creacion del menu de visita
def menu_bolsa():
 
    correcto=False
    num=0
    while(not correcto):
        try:
            num = int(input("Digite la opción deseada: \n"))
            correcto=True
        except ValueError:
            print('Error, introduce una opcion valida')
     
    return num

salir = False
opcion = 0
while not salir:
   
    print("------------WALL STREET------------ \n")
    
    print ("1.-Agregar Una Nueva Empresas")
    print ("2.-Compra de Acciones")
    print ("3.-Venta de Acciones")
    print ("4.-Listado de Empresas Existentes")
    print ("5.-Salir del Sistema\n" )
   
    opcion = menu_bolsa()
 
    if opcion == 1:
        #Se llama a los metodos del sistema mediante el objeto (s) mediante la Uri
        nombre_Empresa=input("Ingrese el nombre de la empresa que se va agregar:")
        print(s.nuevaEmpresa(nombre_Empresa))
    elif opcion == 2:
        #Se llama a los metodos del sistema mediante el objeto (s) mediante la Uri
        codigo_Empresa=int(input("Ingrese el codigo de la empresa: \n"))
        cantidad=int(input("Ingrese la cantidad de acciones que se comprarán:"))
        txt=s.segunda_compra( cantidad,codigo_Empresa)
        print(txt)
    elif opcion == 3:
        #Se llama a los metodos del sistema mediante el objeto (s) mediante la Uri
        codigo_Empresa=int(input("Ingrese el codigo de la empresa(Máximo 4 cifras): \n"))
        cantidad=int(input("Ingrese la cantidad de acciones que se venderán:"))
        txt=s.segunda_venta( cantidad,codigo_Empresa)
        print(txt)
    elif opcion == 4:
        #Se llama a los metodos del sistema mediante el objeto (s) mediante la Uri
        print(s.listar())
    elif opcion == 5:
        salir = True
    else:
        print ("Opción Inválida")
 
print ("Fin del sistema.....!!")