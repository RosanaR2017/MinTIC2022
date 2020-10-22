import sys


def qdigit(m, counter):
    if m//10==0:
        return counter+1
    else:
        counter += 1
        return qdigit(m//10, counter)


def main():
    x=int(input("Ingrese número natural para la cantidad de dígitos:  "))
    print("Resultado : ",qdigit(x,0))
    sys.exit(1)

if __name__== "__main__" :
    main()
