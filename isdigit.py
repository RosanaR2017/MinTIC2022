import sys

def main():
    try:
        x=(input("Enter a digit:"))
        if str(x).isdigit()==True:
            print ("It's a digit")
        else:
            print("It's not a digit")
    except ValueError:  
        sys.exit("Invalid input. You have not enter a string.\n Program ends.")
               
if __name__== "__main__" :
    main()