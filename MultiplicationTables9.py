''' Diseñe un programa que muestre las tablas de multiplicar del 1 al 9. '''

import sys

def mul9():
    m=[]
    for j in range (10):# a list comprehension
        for i in range(10):
            m = m + ["{}X{} = {}".format(j,i,i*j)]
    return m;

def printing(m):
        print("Tablas de multiplicar del 1 al 9:")
        print(*m, sep=" , ")
        

def main():
    try:
        printing(mul9())
    except ValueError:  
        sys.exit("Invalid input. You have not entered m,n integer values correctly separated by a comma.\n Program ends.") 

if __name__== "__main__" :          
    main()