import sys
from math import pi
#import pandas as pd Only in case to use csv. files
import matplotlib.pyplot as plt
import numpy as np


def DrawCircle(h,k,x,y,r1):
 try:
    
    c1= plt.Circle((x,y),radius=r1, color='blue')
    p1= plt.scatter(h,k,color='red')
    ax=plt.gca()
    ax.add_patch(c1)
    plt.axis("scaled")
    plt.axis("on")
    ax.set_title("Circle vs point")
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.legend(["Circle vs point"])
    plt.grid()
    plt.plot(scalex=True, scaley=True)
    plt.show()

 except ValueError:
     print("There is a problem plotting the circle and the point")

 """plt.ylim(-10, 10)
 plt.xlim(-10, 10)"""

 

 plt.show()
 


def InCircle(h, k, x, y, r1):
    if (x-h)**2 + (y-k)**2 <= r1**2:
          return True 
    else:
        return False
   
def main():
    try:
        x, y =(input("Enter x,y cirlce center\' coordinates separated by a comma: ").split(",",2))
        h, k =(input("Enter h,k cirlce point\'s coordinates separated by a comma: ").split(",",2))
        
        r1=float(input("Enter the 1st circle\'s radius: "))
        print(InCircle(float(h),float(k),float(x),float(y),r1))
        DrawCircle(float(h),float(k),float(x),float(y),r1)
    
    except ValueError: 
        sys.exit("Invalid input. You have not entered x,y coordinates separated by a comma.\n Program ends.")
               
if __name__== "__main__" :
    main()