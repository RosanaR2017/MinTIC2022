import sys
import math

def number(x):
    if x==0:
        return "Cero"
    return "Positivo" if x > 0 else "Negativo"

def main():
   
    try:
        list=["4","0","-12","0.0","0","-1"] #input("Please, enter only a list of number separated by a comma.If you enter another key the program will end.\n").split(",")
        list2=[]
        j=0
        
        for i in range(len(list)): 
            
                list2.append(list[i])
                j+=1 
                list2.append(number(float(list[i])))
                j+=1
        a=1   
        print("INPUT"+" "+"OUTPUT")  
        while a <len(list2):
            print("{}     ".format(list2[a-1]),end="\t")
            print("{}".format(list2[a]),end="\n")
            a+=2
        
      

    except ValueError:  
        sys.exit("Invalid input. Program ends.")
               
if __name__== "__main__" :
    main()