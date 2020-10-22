import sys

def even_ASCII(x): #returns True if the value is an even ASCII
    y=ord(x)  #Converts to ASCII
    if  y % 2== 0 and y < 100:
      return True
   
def main():
    try:
        x=(input("Enter a string with a length of 1: "))
        if (len(x)==1):
            if even_ASCII(x):
                print("The first letter of "+ x +" is even of Unicode ASCII value: "+str(ord(x)))
            else:
                print("The first letter of "+ x +" is odd of Unicode ASCII value: "+str(ord(x)))
        else:
            raise ValueError
    except ValueError:  
        sys.exit("Invalid input. You have not enter a string with length 1.\n Program ends.")
               

if __name__== "__main__" :
    main()