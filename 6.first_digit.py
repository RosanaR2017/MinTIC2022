"""Modele mediante una funcion matematica y diseñe un programa
recursivo sin cadenas, tuplas o listas que retorne el primer digito de
un numero natural n (leído de izquierda a derecha). Por ejemplo,
primero(86420) = 8."""

def qdigit(m, counter):
    if m//10==0:
        return counter+1
    else:
        counter += 1
        return qdigit(m//10, counter)

