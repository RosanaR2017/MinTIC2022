import pymongo
from pymongo import MongoClient
from pprint import pprint

mongoClient = ""

try:
    mongoClient = MongoClient('127.0.0.1', port = 27017)
    miDb = mongoClient.tienda #creacion de base de datos
    print(miDb)
    #miCol.drop()
    miCol = miDb.productos #creando la colección
except Exception as e:
    print(type(e),e)

lista_inicial = [
    {'_id':1, 'nombre': "Balón", 'costo': 10000},
    {'_id':2,'nombre': "Chaqueta", 'costo': 85000},
    {'_id':3,'nombre': "Libro", 'costo': 12000},
    {'_id':4,'nombre': "Pantalón", 'costo': 90000},
    {'_id':5,'nombre': "Computador", 'costo': 2500000},
    {'_id':6, 'nombre':"Silla", 'costo': 400000},
    {'_id':7, 'nombre':"Celular", 'costo': 1250000},
    {'_id':8, 'nombre':"Raqueta", 'costo': 250000},
    {'_id':9, 'nombre':"Tablet", 'costo': 600000},
    {'_id':10, 'nombre': "Mesa", 'costo': 172000},
    {'_id':11, 'nombre':"Camiseta", 'costo': 28000},
    {'_id':12, 'nombre':"Cámara", 'costo': 2450000},
    {'_id':13, 'nombre':"Billetera", 'costo': 62000},
    {'_id':14, 'nombre':"Sofá", 'costo': 450000},
    {'_id':15, 'nombre':"Alcancia", 'costo': 15000}
]   
# pprint(lista_inicial)

#miCol.insert_many(lista_inicial)

pprint(miCol)

for x in miCol.find():
    pprint(x)