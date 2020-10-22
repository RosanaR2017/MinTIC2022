import sys
#import numpy

def del_last_digit(m):  #primito  
    return m//10

def qdigit(m, counter):  #Ejercicio 4. 
    if m//10==0:
        return counter+1
    else:
        counter += 1
        return qdigit(m//10, counter)


def del_last_digitv2(m,digitos):  #Ejercicio 3.
    if digitos==1:
        return m
    else:
        m= m-int(m*10**-(digitos-1))*10**(digitos-1)
        return del_last_digitv2(m,digitos-1)


def main():
    x=int(input("Ingrese número natural para otener el último dígito:  "))
    digitos=qdigit(x,0)
    print("Numero de dígitos: {}".format(digitos))
    print("Resultado 'ultimo digito: ",del_last_digitv2(x,digitos))
    sys.exit(1)
    

if __name__== "__main__" :
    main()
