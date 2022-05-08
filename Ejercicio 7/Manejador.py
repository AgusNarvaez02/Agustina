from Viajero import ViajeroFrecuente 
import csv
class Manejador :
    __lista= None
    
    def __init__(self):
        self.__lista=[]
    
    def Crearlista(self):
        archivo= open('archivo.csv')
        reader= csv.reader(archivo,delimiter= ',')
        for fila in reader:
            ob= ViajeroFrecuente(fila[0],fila[1],fila[2],fila[3],fila[4])
            self.__lista.append(ob)
    
               
    def funcion123 (self):
        v= self.__lista[0]
        print(' Igualdad por izquiera \n')
        print(' {} == 100 '.format(v) )
        print(' Igualdad por derecha \n')
        print(' 100 == {} '.format(v) )
        
        print('Apartado 2 \n ')
        v=100 +v
        print('Valores actualizados con millas acumuladas \n')
        v.mostrar()
        
        print ('Canje de millas \n')
        v= 100 - v
        v.mostrar()
