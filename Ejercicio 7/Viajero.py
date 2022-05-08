class ViajeroFrecuente:
    __num_viajero= ''
    __dni=''
    __nombre=''
    __apellido=''
    __millas_acum: int
    
    def __init__(self, num_viajero, dni, nombre, apellido, millas_acum):
        self.__num_viajero= num_viajero
        self.__dni= dni
        self.__nombre= nombre
        self.__apellido= apellido
        self.__millas_acum= int(millas_acum)
        
   
    def GetnumViajero(self):
        return self.__num_viajero
        
    def CantidadTotalMillas(self):
        return self.__millas_acum
    
    def AcumularMillas(self, cant):
        self.__millas_acum+=cant
        return self.__millas_acum
        
    def CanjearMillas(self, canje):
        millas= 0
        if canje<= self.__millas_acum:
            millas= canje-self.__millas_acum
        return millas
    def __eq__(self, otro):
        return self.__millas_acum() == otro
            
    
    def mostrar(self):
        print('Numero de viajero= {}, DNI= {}, Nombre= {}, Apellido= {}, Millas= {}' .format(self.__num_viajero, self.__dni, self.__nombre, self.__apellido, self.__millas_acum ))
    
    def __radd__(self, otro):
        return ViajeroFrecuente(self.__num_viajero, self.__dni, self.__nombre, self.__apellido, self.__millas_acum + otro)
    def __rsub__(self, otro):
        return ViajeroFrecuente(self.__num_viajero, self.__dni, self.__nombre, self.__apellido, self.__millas_acum + otro)
    
