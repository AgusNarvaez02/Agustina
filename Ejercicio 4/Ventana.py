class Ventana:
    __titulo= ''
    __xs= int
    __ys= int 
    __xi= int 
    __yi= int 

    def __init__(self, titulo, xs=1, ys=1, xi=500 , yi=500):
        self.__titulo= titulo
        self.__xs= xs
        self.__ys= ys
        self.__xi= xi
        self.__yi= yi
        if xs<0 or ys<0 or xi>500 or yi>500 or xs>=xi or ys>= yi:
            print('Coordenadas incorrectas')

    def mostrar(self):
         return print('Titulo= ', self.__titulo, ' Vertices superior Izquierdo= ', self.__xs, self.__ys, ' Vertices Inferior Derechos= ', self.__xi, self.__yi)       
    
    def getTitulo(self):
        return print('Titulo: %s', self.__titulo)
    def ancho(self):
        return self.__xi - self.__xs
    def alto(self):
        return self.__yi - self.__ys
    
    def moverDerecha(self, pos=-1):
        if self.__xi+pos>=0:
            self.__xi+=pos
        if self.__xs+pos <=500:
            self.__xs+=pos
    def moverIzquierda(self, pos=1):
        if self.__xi-pos>=0:
            self.__xi-=pos
        if self.__xs-pos <=500:
            self.__xs-=pos
    
    def bajar(self, pos=-1):
        if self.__yi-pos>=0:
            self.__yi-=pos
        if self.__ys-pos<=500:
            self.__ys-=pos
            
    def subir(self, pos=1):
        if self.__yi+pos>=0:
            self.__yi+=pos
        if self.__ys+pos<=500:
            self.__ys+=pos
    
    
