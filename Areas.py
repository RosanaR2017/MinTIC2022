from math import pi
import sys

def ErrorPrint():
    print("Entrada no válida, finaliza el programa")
    sys.exit(1)
    
def num(n):
    while True: 
        try:
            n=int(n)

            return n;
        except ValueError: 
            try:
                n=float(n) 
                return n;                    
            except ValueError: 
                ErrorPrint()
                break

def positivo(n):
    if (n>0 and n!=0):
        return n;
    else:
        ErrorPrint();

def AreaCircle(radius):
    positivo(num(radius))
    return str(pi*(radius**2))

def AreaRect(base, height):
    positivo(num(base*height))
    return str(base*height);

def main():

    areaType=str(input("Ingrese el tipo de area a calcular:")) #Solo circulo o rectangulo

    if areaType.casefold() == "Circulo".casefold():
        radio=positivo(num(input("Ingrese radio:")))
        print("\nArea Circulo:{}".format(AreaCircle(radio)))
    elif areaType.casefold() == "Rectangulo".casefold():
        base, height= input("Ingrese base y altura separados por una coma:").split(",")
        print("\nArea Rectangulo:{}".format(AreaRect(positivo(num(base)),positivo(num(height)))))
    else:
        sys.exit(1)    
        print("wESSaaaaa".upper())
        #ErrorPrint()

if __name__=='__main__':
    main()
