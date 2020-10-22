import sys

def descending_number():
    for i in range(99,1,-1):
        print(i,end=",")

   
def main():

    descending_number()
    print(1)  # I add this line to end without a comma.
    sys.exit(1)

if __name__== "__main__" :          
    main()