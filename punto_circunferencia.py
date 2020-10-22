#*****************PROBLEMA CIRCUNFERENCIA*****************
import math 
#leyendo el centro del circulo de coordenadas h y k y el radio r
h = float(input("Ingrese la coordenada h para el centro: "))
k = float(input("Ingrese la coordenada k para el centro: "))
r = float(input("Ingrese el radio r: "))
#Leyendo R2 asumiendo que es un punto de coordenadas x1 y1
x1 = float(input("Ingrese la coordenada x1 de R2: "))
y1= float(input("Ingrese la coordenada y1 de R2: "))

def hallarRangoX(h, k, x1, y1, r):
    max = h + (abs(r**2 - (y1 - k)**2))**(1/2)
    min = h - (abs(r**2 - (y1 - k)**2))**(1/2)
    if x1 < max and x1 > min:
        return True
    else:
        return False

def hallarRangoY(h, k, x1, y1, r):
    max = k + (abs(r**2 - (x1 - h)**2))**(1/2)
    min = k - (abs(r**2 - (x1 - h)**2))**(1/2)
    if y1 < max and y1 > min:
        return True
    else:
        return False

if hallarRangoX(h, k, x1, y1, r) and hallarRangoY(h, k, x1, y1, r):
    print("El punto de coordenadas ", x1, ", ", y1, " si pertenece al circulo")
else:
    print("El punto no esta dentro del circulo")


