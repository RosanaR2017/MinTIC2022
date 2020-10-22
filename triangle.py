import sys
from math import pi

def Triangle(a,b,c):
      if ( a < b + c) and (a > abs(b-c)):
          return True 
      else:
        return False
   
def main():
    try:
        a,b,c=(input("Enter a,b,c which are the triangle's lengths separated by a comma: ").split(",",3))  
        print(Triangle(float(a),float(b),float(c)))
        print(Triangle)
    except ValueError:  
        sys.exit("Invalid input. You have not entered l1,l2,l3 separated by a comma.\n Program ends.")
               
if __name__== "__main__" :
    main()