class Email:
    __idCuenta=''
    __dominio= ''
    __tipoDominio= ''
    __contraseña= ''
    
    def __init__(self, idCuenta, dominio, tipoDominio, contraseña):
       self.__idCuenta= idCuenta
       self.__dominio= dominio
       self.__tipoDominio= tipoDominio
       self.__contraseña= contraseña
    def getDominio(self):
        return self.__dominio
    def retornaemail(self,nombre):
        return ("Estimado "+ nombre + " te enviaremos un mensaje a la direccion " + self.__idCuenta + "@" + self.__dominio + "." + self.__tipoDominio)
    
    
def modificar (self, actual, regis):
    if actual == regis:
        actual= input("Ingrese nueva contraseña: ")
        return actual
    else:
        input ("Contraseña invalida")
   
    def Crear_cuenta(self,correo):
        adr= correo.split("@")
        tip= adr[1].split(".")
        self.idCuenta= adr[0]
        self.dominio= tip[0]
        self.tipoDominio= tip[1]
        
        
    def ejer4 (direc):
        lista=[]
        for i in range (len(direc)):
            ad= Email("","","","")
            ad.Crear_cuenta(direc[i])
            lista.append(ad)
            busca= input("ID para buscar : ")
            b=0
            for ad in lista:
                if ad.idCuenta == busca:
                    b=1
            if b==1 :
                print ("El Id se encuentra repetido")
            
            else:
                print ("No se encontro el ID ")
        
