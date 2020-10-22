import sys

def sumatoria(n):
    if n==0:
        return 0
    else:
        return sumatoria(n-1)+n


def main():
    x=int(input("Ingrese número natural para el cálculo de su sumatoria:  "))
    print("Resultado sumatoria: ",str(sumatoria(x)))
    sys.exit(1)
if __name__== "__main__" :
    main()




