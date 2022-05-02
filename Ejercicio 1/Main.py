from Email import Email
import csv

if __name__== '__main__':
    nom = input("Ingrese nombre: ")
    
    x = Email(input ("Ingrese su ID:"),input ("Ingrese su dominio:"),input ("Ingrese su tipo de dominio:"),input ("Ingrese su contraseña:"))
    
    print (x.retornaemail(nom))
    
    x.contraseña= modificar(input("Ingrese contraseña actual: "), x.contraseña)
        
    cor= Email("","","","")
    cor.Crear_cuenta(input("Ingrese Correo: "))
    print(cor.Crear_cuenta()) 
    
    archivo= open("Correos.csv")
    direccion = archivo.read() .split(",")
    
    ejer4(direccion)
    archivo.close()
    
