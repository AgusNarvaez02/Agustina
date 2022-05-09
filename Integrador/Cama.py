class cama:
    __idCama: int
    __habitacion: int
    __estado: bool
    __nomyap=''
    __diagnostico= ''
    __fechaint= ''
    __fechaalta: str= None
    
    def __init__(self, idCama, habitacion, estado, nomyap, diagnostico, fechaint, fechaalta):
        self.__idCama= int(idCama)
        self.__habitacion= int(habitacion)
        self.__estado= bool(estado)
        self.__nomyap= nomyap
        self.__diagnostico= diagnostico
        self.__fechaint= fechaint
        self.__fechaalta= str(fechaalta)
    
    def __str__(self):
        return ("idCama: {} - Habitacion: {} - NyA: {} - Diagnostico: {} - Fecha de Internacion: {}".format(self.__idCama ,self.__habitacion, self.__nomyap, self.__diagnostico, self.__fechaint))
    
    def getidCama(self):
        return self.__idCama
    def getfechaalta(self):
        return self.__fechaalta
    def gethab (self):
        return self.__habitacion
    def getest (self):
        return self.__estado
    def getnomyap(self):
        return self.__nomyap
    def getdiag(self):
        return self.__nomyap
    def getfechaint(self):
        return self.__fechaint
    def set_fechaalt (self, fecha):
        self.__fechaalta= fecha
        self.__estado= False
