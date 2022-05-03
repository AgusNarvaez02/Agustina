from Manejador import Manejador
class Menu:
    __ini= None
        
    def __init__(self):
        self.__ini= Manejador()
        self.__ini.cargaLista()
        
    def CrearMenu (self):
        print('1. Actualizar valor de vehiculo de cada plan \n\n 2.Dado un valor, mostrar\n\n 3. Monto para licitar Vehiculo \n\n 4.Modificar cantidad de cuotas\n')
        op= int(input('Ingrese una opcion '))
        while op!= 0:
            if op== 1:
                self.__ini.opcion1()
            elif op== 2:
                val= float(input('Ingrese un valor: \n '))
                b= self.__ini.opc2(val)
                if b!= -1:
                    print('Codigo del plan= {} \n\n Modelo= {} \n\n Version del vehiculo= {} ' .format(self.__ini.getcod(b),self.__ini.getmod(b),self.__ini.getversion(b)))
            elif op== 3:
                self.__ini.opcion3()
            elif op== 4:
                cod= int(input('Ingrese codigo de un plan '))
                c= self.__buscar(cod)
                if c!=-1:
                    n= int(input('Ingrese nueva cantidad de cuotas para licitar: ')) 
                    self.__ini.opcion4(n)
                    
                else: print('Codigo incorrecto')
            else: print('Opcion incorrecta')
        print('1. Actualizar valor de vehiculo de cada plan \n\n 2.Dado un valor, mostrar\n\n 3. Monto para licitar Vehiculo \n\n 4.Modificar cantidad de cuotas\n')
        op= int(input('Ingrese una opcion '))
        
         
