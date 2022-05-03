class PlanAhorro:
    __cod=0
    __modelo= ''
    __version=''
    __valor= 0.0
    __cuotas_plan= 84
    __cuotas_lic= 15
    
    def __init__(self, cod, modelo, version, valor):
        self.__cod= cod
        self.__modelo= modelo
        self.__version= version
        self.__valor= valor
        #self.__cuotas_plan= cuotas_plan
        #self.__cuotas_lic= cuotas_lic
    
    def getcod(self):
        return self.__cod
    def getmod (self):
        return self.__modelo
    def getversion(self):
        return self.__version
    
    def __str__(self):
        return '%d %s %s %d'%(self.__cod,self.__modelo,self.__version, self.__valor)
    def valor(self):
        return self.__valor
    
    @classmethod
    def getcuotplan(cls):
        return cls.__cuotas_plan
    
    @classmethod
    def getcuotlic(cls):
        return cls.__cuotas_lic
    
    def mod_precio(self, act):
        self.__valor=act
    
    def getvalorcuota (self):
        return (self.__valor/self.__cuotas_plan) + self.__valor *0.10
    def getmonto (self):
        p= self.getvalorcuota
        return float(self.__cuotas_lic * p) 
    
    
    @classmethod
    def setValorCuotasPlan(cls, nuevovalor):
        cls.__cuotas_lic =nuevovalor

    
    
