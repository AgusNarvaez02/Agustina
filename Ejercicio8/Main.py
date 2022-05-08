from Conjunto import Conjunto

if __name__ == '__main__':
    cA= Conjunto([1,2,3,4])
    cB= Conjunto([1,2,5,4])
    print(' 1. Suma\n 2. Resta \n 3.Igualdad \n')
    op= int(input ('\nElija una opcion (0 para salir) \n'))
    
    while op != 0:
        
        if op == 1:
           print(' A + B= {}' .format(cA + cB))
        elif op== 2:
            print(' A - B= {}' .format(cA - cB))
        elif op== 3:
            print(' A == B= {}' .format(cA == cB))
        print('-----------------')
        print(' 1. Suma\n 2. Resta \n 3.Igualdad \n')
        op= int(input ('\nElija una opcion (0 para salir) \n'))
         
