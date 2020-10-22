'''Problema: A un niño pequeño le gusta escribir al reves. Sin embargo ha escrito unas cadenas muy largas y se tiene la traducción. El necesita su ayuda para saber si lo que ha escrito al revés es lo mismo que piensa. '''
''' --------------------------------------------------------------------------------
Entrada:
Dos Strings uno con la cadena al derecho y otro con la posible cadena invertida.

Salida:
La palabra SI si la palabra corresponde a su versión invertida.  La palabra NO en caso contrario.
-------------------------------------------------------------------------------- '''
import sys

def palindrome(s1,s2):
    l1=len(s1) #Returns the length of the string l1
    l2=len(s2) #Returns the length of the string l2  
    s3=""      #An empty string is created to compare s1 and s2
    for i in range(l1-1,-1,-1):
      s3=s3+s1[i]
    
    if s3==s2:
      return "SI"
    return "NO"

def main():
    try:
        s1=input("Ingrese cadena al derecho:")
        s2=input("Ingrese cadena invertida:")
        print(palindrome(s1,s2))

    except ValueError:  
        sys.exit("Entrada no carácteres no válida.") 

if __name__== "__main__" :          
    main()