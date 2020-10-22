import pymongo
from pymongo  import MongoClient
import sys


def connectionDB():
    try:
        mongoClient = MongoClient('127.0.0.1', port= 27017)
        print(mongoClient.list_database_names())  #List all the databases
        miDb = mongoClient.restaurante # Base de datos restaurante creada.
        print(miDB)
        return miDB
    Exception as e:
        print("Problemas de conexión o creación de la base de datos")


def insertProd():
        miProducto = {
    "_id" : 1,
    "nombre" : "BigBurger",
    "precio" : 25000,
    "existencias" : 30,
    "categoría" : "Hamburguesa",
    "ingredientes" : {
        "pan" : "arabe",
        "salsa" : ["tomate", "mayonesa"],
        "vegetales" : ["lechuga", "tomate"]
    }
    }
        return miProducto

def main():
    miDB=connectionDB()
    print(miDB)



if __name__== "__main__" :
    main()
