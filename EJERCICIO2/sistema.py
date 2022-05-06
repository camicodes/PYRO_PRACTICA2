import Pyro4

class Emprendimiento:
     #inicializar los atributos del objeto
    def __init__(self,nombre,codigo):
        self.nombre=nombre
        self.codigo=codigo
        self.acciones=100
        self.valor=10000
    def primera_compra(self,num):
        self.acciones=self.acciones-num
        self.valor=self.valor+(10*num)
    def primera_venta(self,num):
        self.acciones=self.acciones+num
        self.valor=self.valor-(10*num)
@Pyro4.expose

class Bolsa_valores:
    emprendimientos=[]
    registro=[]
    def nuevaEmpresa(self,nombre):
        codigo=len(self.emprendimientos)+1
        self.emprendimientos.append(Emprendimiento(nombre,codigo))
        #Imprime el nombre de la empresa agregada
        #Se agrega un parametro para dar validación al nombre ingresado de la empresa
        txt='La Empresa '+nombre+' se agregó a la bolsa de valores'
        print(txt)
        return txt
    def listar(self):
        txt='Empresa- '+'Codigo- '+'Acciones- '+'Valor'+'\n'
        #En caso válido de agregar más empresas, se enlistará al final de cada una
        for i in self.emprendimientos:
            #Imprime el nombre, codigo, acciones y valores de las empresas existentes
            txt=txt+str(i.nombre)+'\t'+str(i.codigo)+'\t'+str(i.acciones)+'\t'+str(i.valor)+'\n'
        print(txt)
        return txt
        
    def segunda_compra(self,num,codigo):
        for i in self.emprendimientos:
            if(i.codigo==codigo):
                i.primera_compra(num)
                #Se agrega un parametro para dar validación al cantidad de las acciones compradas de la empresa
                txt='Fueron compradas '+str(num)+' de acciones en la Empresa '+i.nombre
                print(txt)
                return txt
    def segunda_venta(self,num,codigo):
        for i in self.emprendimientos:
            if(i.codigo==codigo):
                i.primera_venta(num)
                #Se agrega un parametro para dar validación la cantidad de acciones vendidas de la empresa
                txt='Fueron vendidas '+str(num)+' de acciones de la Empresa '+i.nombre
                print(txt)
                return txt
                




