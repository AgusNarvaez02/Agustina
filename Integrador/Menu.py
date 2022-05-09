from ManejadorCama import ManejadorCama
from ManejadorMed import ManejadorMedic

class Menu:
    __insCama= ManejadorCama()
    __insMedic= ManejadorMedic()
    
    def __init__(self):
        self.__insCama= ManejadorCama()
        self.__insMedic= ManejadorMedic()
        self.__insCama.cargar()
        self.__insMedic.cargalista()
    
    def op3 (self):
        p= input('Ingrese Nombre y apellido de un paciente internado \n')
        b= self.__insCama.buscarpaciente(p)
        if p!= -1:
            fa= input('Ingrese fecha de alta')
            self.__insCama.alta(fa, b)
            self.__insCama.mostrar_paci(b)
            c= self.__insCama.getidCama(b)
            
            self.__insMedic.infromacion(c)
    def Menuop(self):
        print('1. Manejador Cama \n 2.Crear Manejador Medicamento \n 3. Datos de un paciente \n 4. Paciente internado')
        op= int(input('Ingrese una opcion \n'))
        
        while op != 0:
            if op== 1:
                self.__insCama.mostrar()
            
            if op==2:
                self.__insMedic.mostrar()
            if op==3:
                self.op3()
            if op==4:
                self.__insCama.datos_internado()
            
            print('1. Manejador Cama \n 2.Crear Manejador Medicamento \n 3. Datos de un paciente \n 4. Paciente internado')
            op= int(input('Ingrese una opcion \n'))
            
