import sys

def odd_from123_140():
    for i in range(123,138,2):
        print(i,end=",")
  

def main():
    odd_from123_140() #Call the function that calculates prints the odd from 123 to 137
    print("139")
    sys.exit(1)


if __name__== "__main__" :          
    main()