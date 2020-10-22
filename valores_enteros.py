import sys

def main():
    try:
        # These lines convert all the values into integers.
        A=float(input("A:"))  
        B=float(input("B:")) 
        C=float(input("C:")) 
        D=float(input("D:")) 
        if (B>C and D>A and C+D > A+B and C>0 and D>0 and A%2==0):
            print("Valores aceptados") 
        else:
            print("Valores no aceptados") 

    except ValueError:  
        sys.exit("Invalid input. You have not entered integer values correctly separated by a comma.\n Program ends.") 

if __name__== "__main__" :          
    main()

