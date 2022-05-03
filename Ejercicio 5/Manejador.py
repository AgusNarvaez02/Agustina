from PlanAhorro import PlanAhorro
import csv
class Manejador :
    __lista= None
    
    
    
    def __init__(self):
        self.__lista= []
    
    def cargaLista(self):
        archivo= open('planes.csv')
        reader= csv.reader (archivo, delimiter= ';')
        for fila in reader : 
            objeto = PlanAhorro(int(fila[0]), fila[1], fila[2], float(fila[3]))
            self.__lista.append(objeto)
    
    def opcion1(self):
        for i in range(len(self.__lista)):
            print(' Codigo del plan {} \n Modelo del vehiculo= {} \n Version del vehiculo= {}'.format(self.__lista[i].getcod(), self.__lista[i].getmod(),  self.__lista[i].getversion()))
            act= float(input('Ingrese precio actual: '))
            print('Precio actual {}' .format(self.__lista[i].mod_precio(act)))
            
            
    def opc2(self, val):
        r= -1
        i= 0
        ban= False
        while i< len(self.__lista) and ban==False:
            if self.__lista[i].getvalorcuota() < val:
                ban= True
                r= i
            else:
                i+=1
        return r
    
    def opcion3 (self):
        for i in range(len(self.__lista)):
            print('Para licitar el vehiculo con codigo {} se debe haber abonado {}' .format(self.__lista[i].getcod(), self.__lista[i].getmonto()))
     
    def buscar (self, cod):
        i=0
        r=-1
        ban= False
        while i< len(self.__lista) and ban == False:
            if self.__lista[i].getcod() ==cod:
                ban= True
                r= i
            else:
                i+=1
        return r
    #@classmethod()
    def opcion4 (self, c):
        print('Nueva cantidad de cuotas {}' .format(self.__lista.modifica(c)))
        
        
