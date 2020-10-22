import sys

def dist(p1,p2):
    d= ((p1[0]-p2[0])**2 +(p1[1]-p2[1])**2 +(p1[2]-p2[2])**2)**(1/2)
    return d


def main():
    try:
        p1 = tuple(map(int, input().split(' '))) #"Please enter x1,y1,z1:\n"
        p2 = tuple(map(int, input().split(' '))) #"Please enter x2,y2,z2:\n"
        print(dist(p1,p2))
    except ValueError:  
        sys.exit("Invalid input. You have not entered m,n integer values correctly separated by a comma.\n Program ends.") 

if __name__== "__main__" :          
    main()