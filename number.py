import sys

def number(x):
    if x==0:
        return print("The number {}".format(x)+" is a neutral number")
    return print("The number {}".format(x)+" is positive") if x > 0 else print("The number {}".format(x)+" is negative")
        

def main():
    try:
        x=float(input("Enter a number: "))
        number(x)
    except ValueError:  
        sys.exit("Invalid input. You have not enter a float.\n Program ends.")
               
if __name__== "__main__" :
    main()