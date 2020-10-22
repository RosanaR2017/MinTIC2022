import sys

def last_digit(n,x):
    if n-x < 10:
        return n%10
    else:
        return last_digit(n-x,x*10)


def main():
    n=int(input("Ingrese número natural para otener el último dígito:  "))
    print("Resultado : ",last_digit(n,10))
    sys.exit(1)

if __name__== "__main__" :
    main()