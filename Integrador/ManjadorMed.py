from Medicamento import Medicamento
import csv
class ManejadorMedic:
    lista=[]
    
    def __init__(self):
        self.__lista=[]
    
    def cargalista(self):
        archivo= open('medicamentos.csv')
        reader= csv.reader(archivo, delimiter=';')
        next(reader, None)
        for fila in reader:
            obj= Medicamento(fila[0],fila[1],fila[2],fila[3],fila[4],fila[5],fila[6])
            self.__lista.append(obj)
        archivo.close()
    def mostrar (self):
        for elem in self.__lista:
            print('{}' .format(elem))
    
    def infromacion(self, c):
        t=0
        for i in range(len(self.__lista)):
            if self.__lista[i].getidCam == c:
                t=0
                print(' Monodroga\t\t Presentacion\t\t Cantidad\t\t Precio\n')
                print(' {}\t\t {}\t\t {}\t\t {}\t\t'.format(self.__lista[i].getmonod(), self.__lista[i].getpres(), self.__lista[i].getcant(), self.__lista[i].getpres()))
                t+= self.__lista[i].getpres()
        print('Total adeudado {}'.format(t))
    
        
