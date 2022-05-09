class Medicamento :
    __idCama: int
    __idMedicamento: int
    __nom= ''
    __monodroga=''
    __presentacion= ''
    __cant= ''
    __total: float
    
    def __init__(self, idCama, idMedicamento, nom, monodroga, presentacion, cant, total):
        self.__idCama= int(idCama)
        self.__idMedicamento= int(idMedicamento)
        self.__nom= nom
        self.__monodroga= monodroga
        self.__presentacion= presentacion
        self.__cant= cant
        self.__total= float(total)
        
    def __str__(self):
        return('{},{},{},{},{},{},{}' .format(self.__idCama, self.__idMedicamento, self.__nom, self.__monodroga,self.__presentacion, self.__cant, self.__total))
               
    def getidCam (self):
        return self.__idCama
    def getidMed (self):
        return self.__idMedicamento
    
    def getnom(self):
        return self.__nom
    def getmonod(self):
        return self.__monodroga
    
    def getpres(self):
        return self.__presentacion
    def getcant(self):
        return self.__cant
    def getot(self):
        return self.__total
    
