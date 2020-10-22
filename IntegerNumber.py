"""PROBLEMA: Dado un número entero n y otro entero m, escriba un programa que muestre los múltiplos de m hasta n.
Entrada
Los números n y m. Para este laboratorio es necesario que al leer n y m agrege los mensajes "digite n:" y "digite m:"
Salida
Como salida se debe mostrar el aviso"""

import sys

def IntegerNumber(n,m):   # función que determina los múltiplos de m hasta n.
   
    list_m=[] #List of multiples. 
    
    list_m=range(0,n+1,m) 
    return list_m

def main():
    try:
        n=int(input("digite n: "))
        m=int(input("digite m: "))
        list_m= IntegerNumber(n,m)

        print("Los múltiplos son:\n")
        for i in list_m:
            print(i) #Printing the list.

    except ValueError:  
        sys.exit("Invalid input. You have not entered m,n integer values correctly separated by a comma.\n Program ends.") 

if __name__== "__main__" :          
    main()