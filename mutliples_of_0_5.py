import sys

def multiples_of_0_5():
    for i in range(0,46,5):
        print(i,end=",")
   
def main():

    multiples_of_0_5()
    print(45)  # I add this line to end without a comma.
    sys.exit(1)

if __name__== "__main__" :          
    main()