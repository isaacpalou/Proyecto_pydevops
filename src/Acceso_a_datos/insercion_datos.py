import pymongo
import json
from conexion_bd import conexion_bd


def insertar_item():
    collection = conexion_bd()
    newItem = {'item'}
    collection.insert_one(newItem)


def borrar_item():
    collection = conexion_bd()
    Item = {'item'}
    collection.delete_one(Item)


# def insercion_datos():
#     collection = conexion_bd()
#     with open("src/Acceso a datos/menus.json", "r") as my_json:
#         datos = json.load(my_json)
#     try:
#         collection.insert_many(datos)
#         print("DATOS METIDOS CON ÉXITO")
#     except pymongo.errors.ServerSelectionTimeoutError as error:
#         print("Error al conectar al servidor") % error
#     except pymongo.errors.CollectionInvalid as error:
#         print("No se pudo conectar a MongoCompass") % error


# def borrar_coleccion():
#     collection = conexion_bd()
#     collection.drop()
