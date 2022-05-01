from Viajero import ViajeroFrecuente
import csv
class Manejador_Viajeros:
    __lista= []
    
    def __init__(self, lista):
        self.__lista=[]
    
    def CargaLista (self, viaj):
        archivo= open('archivo.csv')
        reader= csv.reader(archivo,delimiter=',')
      
        for fila in reader : 
            objeto = ViajeroFrecuente(fila[0], fila[1], fila[2], fila[3], fila[4])
            self.__lista.append(objeto)
            
    def BuscarViajero (self, num):
        retorno= -1
        i=0
        ban= False
        While (i < len(self.__lista) and (ban == False):
            if num == self.__lista[i].GetnumViajero:
                ban= True
                retorno= i
            else:
                i+=1
            return retorno()
    
    def Op1  (self, retorno):
        self.lista[retorno].CantidadTotalMillas
        
    def Op2 (self, retorno):
        c= int(input('Ingrese cantidad de millas para acumular: '))
        self.__lista[retorno].AcumularMillas(c)
    
    def Op3 (self, retorno):
        canje= int(input('Ingrese millas a canjear: '))
        n= self.__lista.CanjearMillas(canje)
        if n!= 0:
            print('Cantidad de millas= {}', n)
        else:
            print("Error")
        
        
        
