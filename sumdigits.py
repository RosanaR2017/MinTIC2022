import sys


def recurSum(n,counter):
    if n == 0:
        return counter
    else:
        counter=counter+n%10 
    return recurSum(n//10,counter)


def main():
    n=int(input("Ingrese la suma para calcular un número natural n:  "))
    print("Resultado : ",recurSum(n,0))

if __name__== "__main__" :
    main()