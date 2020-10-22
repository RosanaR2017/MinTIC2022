import math  # Se pide que que se utilice Math.PI

def area_circulo(r):
# r corresponde al radio del círculo
    return math.pi*r*r

def area_rectangulo(l, a):
    """ Input: l correspondiente al largo
    a correspondiente al ancho Returns: área del rectángulo"""
    return l*a

def area_carro(a1,b1,a2,b2,r1,r2):
    # area circulo 1+area circulo 2+ area rectangulo 1 +area rectangulo 2)
    return(area_circulo(r1)+area_circulo(r2)+area_rectangulo(b1,a1)+area_rectangulo(b2,a2))

def main():
    a1=float(input("")) #Entradas - Ingrese altura a1: 
    b1=float(input("")) #Ingrese base b1: 
    a2=float(input(""))  #Ingrese altura a2: 
    b2=float(input(""))  #Ingrese base b2: 
    r1=float(input(""))  #Ingrese radio r1: 
    r2=float(input(""))  #Ingrese radio r2: 

    print("suma total = ", area_carro(a1,b1,a2,b2,r1,r2)) # Se imprime el area total del carro

if __name__== "__main__" :
    main()