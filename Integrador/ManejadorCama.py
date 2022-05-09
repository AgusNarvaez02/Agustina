from Cama import cama
import numpy as np
from numpy import array
import csv

class ManejadorCama:
    __arreglo: array
    
    def __init__(self):
        self.__arreglo= self.cargar()
        
    def cargar(self):
        lista=[]
        archivo= open('camas.csv')
        reader=csv.reader(archivo,delimiter=';')
        next(reader,None)
        for fila in reader:
           obj=cama(fila[0],fila[1],fila[2],fila[3],fila[4],fila[5], fila[6])
           lista.append(obj)
        
        a=np.array(lista)
        return a
    
    def mostrar(self):
        for i in range(len(self.__arreglo)):
            print(self.__arreglo[i])
    
    def buscarpaciente(self,p):
        i= 0
        retorno= -1
        band= False
        while i< len(self.__arreglo) and band== False:
            if self.__arreglo[i].getnomyap== p:
                band= True
                retorno= i
            else: i+=1
        return retorno
    def alta (self, fa, b):
        self.__arreglo[b].set_fechaalt= fa
    
    def mostrar_paci(self, b):
        print('Paciente: {} \t Cama: {} \t Habitacion: {} \n' .format(self.__arreglo[b].getnomyap(), self.__arreglo[b].getidCama(), self.__arreglo[b].gethab()))
        print('Diagnostico: {} \t Fecha de internacion: {} \n'.format(self.__arreglo[b].getdiag(), self.__arreglo[b].getfechaint()))
        print ('Fecha de alta {} |n'.format(self.__arreglo[b].getfechaalta()))
    
    def datos_internado(self):
        d= input('Ingrese diagnostido del paciente \n')
        for i in range(len(self.__arreglo)):    
            if self.__arreglo[i].getdiag == d:
                if self.__arreglo.getest == True:
                    print(self.__arreglo[i])
            else:
                print('El paciente {} no posee el diagnostico ingresado o fue dado de alta \n' .format(self.__arreglo[i].getnomyap))
           
