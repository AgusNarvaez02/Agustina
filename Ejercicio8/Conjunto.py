class Conjunto:
    __lista= list
    
    def __init__(self, lista):
        self.__lista= lista
    def __str__(self):
        return str(self.__lista)
    def __add__( self, otro):
        c= []
        for el in self.__lista:
            c.append(el)
        for el in otro.__lista:
            if el not in c:
                c.append(el)
                
        return Conjunto(c)

    def __sub__ (self, otro):
        c=[]
        for i in self.__lista:
            if i not in otro.__lista:
                c.append(i)
                
        return Conjunto(c)
    def __eq__ (self, otro):
        band= False
        if len(self.__lista)== len(otro.__lista):
            band= True
        for i in self.__lista:
            if i not in otro.__lista:
                    band= False
        
        return band
            
    
