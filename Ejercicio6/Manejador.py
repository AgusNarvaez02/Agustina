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
    
    def Mayor (self):
        m= self.__lista[0]
        for i in range(len(self.__lista)):
            if self.__lista[i]>m:
                m= self.__lista[i].CantidadTotalMillas()
        return m
                
    def comparar (self):
        b= self.Mayor()
        for i in range(len(self.__lista)):
            if self.__lista[i].CantidadTotalMillas() == b:
                print('El viajero {} tiene la misma cantidad de millas que la mayor cantidad de millas acumuladas ' .format(self.__lista[i].GetnumViajero()))
               
    def funcion23 (self):
        v= self.__lista[0]
        v+=100 
        print('Valores actualizados con millas acumuladas \n')
        v.mostrar()
        print ('Canje de millas \n')
        v-=100
        v.mostrar()
    
    
    
                
