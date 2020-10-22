import sys

def fraction_(a,b,n):
    if n > a or n > b:
     return a, b
    if a==b:
     return 1, 1
    elif a%n == 0 and b%n == 0:
      return fraction_(a/n,b/n,n)
    else:
      return fraction_(a,b,n+1)

def main():
    x,y=map(int,input("Ingrese una fracción separada por \"/\":").split("/"))
    x,y=map(int,fraction_(x,y,2))
    print(x,y,sep="/")

if __name__== "__main__" :
    main()