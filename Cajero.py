import sys
def Salida():
    peticion=input("Error:dato invalido.\nSi desea salir del programa entre la llave \'si\':")
    if(peticion=="si".capitalize()):
        sys.exit("Ha salido usted del programa")    
    else:
        retiro()
        return;

def retiro(): #  Comprobación retiro de 10000
    ret=float(input("")) #Ingrese cantidad a retirar:
    if( ret % 10000!=0):
        Error1000=ValueError("El monto a retirar no es multiplo de 10000.")
        Salida();
    else:
        return ret;

def main():
    billetes = [100000,50000,20000,10000] # denominaciones de billetes presente
    ret= retiro()
    
    for bills in billetes: 
        print("{:.0f}".format(ret//bills)+" x ${}".format(bills)) # numero de billetes y denominación
        ret=ret-(ret//bills)*bills
        
if __name__== "__main__" :
    main()