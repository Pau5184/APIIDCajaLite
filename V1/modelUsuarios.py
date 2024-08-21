from pymongo import MongoClient
from bson import ObjectId
from bson.binary import Binary
import base64

class Conexion():
    def __init__(self, db_name):
        self.cliente = MongoClient("mongodb+srv://apbarajas658:32GeaC79hqdZNTbf@cluster0.6f3klmh.mongodb.net/")
        self.db = self.cliente[db_name]

    def obtenerUsuario(self, data):
        resp = {"estatus":"","mensaje":""}
        usuario = self.db.Usuarios.find_one({"usuario":data["usuario"],"password":data["password"]})
        if usuario:
            resp["estatus"]="ok"
            resp["mensaje"]="Usuario encontrado"
            resp["usuario"]={"_id":str(usuario["_id"]), "nombre":usuario["nombre"], "apPaterno":usuario["apPaterno"], "apMaterno":usuario["apMaterno"], "usuario":usuario["usuario"]}
        else:
            resp["estatus"]="error"
            resp["mensaje"]="Usuario no encontrado"
        return resp