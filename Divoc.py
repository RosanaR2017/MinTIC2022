"""PROBLEMA: A partir del día 1, el país A tiene una población contagiada de Divoc 9012 de n (1 <=n <= 10^8) y el país B tiene una población contagiada de Divoc 9012 de m (1 <= m <= n). Las tasas de crecimiento diario son de 2% y 3% respectivamente. Desarrollar un algoritmo para informar en que día la población contagiada del país B iguala o supera a la del país A.
Entrada
La entrada consta de dos números reales que representan la cantidad de gente contagiada.
Salida
El día en el cual la población contagiada del país B supera la del país A"""

import sys

def Divoc(n,m):   # n is country's A population and m is country's B population
    if (1<=n<=10E8) and (1<=m<=n):
        day=1     #This is day one 
        while(m<n):
            n+=n*0.02  # country's A infected population increase rate.
            m+=m*0.03  # country's B infected population increase rate.
            day+=1     #Increase the days counter.
        
        print(day)
    else:
        sys.exit("You have entered an invalid population value")
  
def main():
    try:
        n=int(input("Enter n integer values which represents  country's A infected population with Divoc: "))
        m=int(input("Enter m integer values which represents  country's B infected population with Divoc: "))
        Divoc(n,m)
    except ValueError:  
        sys.exit("Invalid input. You have not entered m,n integer values correctly separated by a comma.\n Program ends.") 

if __name__== "__main__" :          
    main()