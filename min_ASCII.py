import sys

def min_ASCII(x): #returns True if the value is a lower case vowel
    vocal=['a','e','i','o','u']
    return vocal.__contains__(chr(x))


def main():
    try:
        x=int(input("Input an integer number that represents a lower case vowel:"))

        if min_ASCII(x): # Here x indicates if we have an ASCII value using the function min_ASCII
            print("The number {}".format(x)+" represents character:"+chr(x))
        else:
            print("The number {}".format(x)+" represents character:"+chr(x)+", which is not a lower case vowel")

    except ValueError:  
        sys.exit("Invalid input. You have not enter an integer.\n Program ends.")
               

if __name__== "__main__" :
    main()