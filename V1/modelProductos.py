from pymongo import MongoClient
from bson import ObjectId
from bson.binary import Binary
import base64

class Conexion():
    def __init__(self):
        self.cliente = MongoClient("mongodb+srv://apbarajas658:32GeaC79hqdZNTbf@cluster0.6f3klmh.mongodb.net/")
        self.db = self.cliente.IDCajaLite
        
    def registrarProducto(self, data):
        resp = {"estatus":"","mensaje":""}
        producto=self.db.Productos.find_one({"codigoBase":data["codigoBase"]})
        if producto:
            resp["estatus"]="error"
            resp["mensaje"]="El producto ya existe"
        else:
            image_binary = base64.b64decode(data['foto'])
            data['foto'] = Binary(image_binary)
            self.db.Productos.insert_one(data)
            resp["estatus"]="ok"
            resp["mensaje"]="Producto registrado"
        return resp
    
    def obtenerProductos(self):
        resp={"estatus":"", "mensaje":""}
        productos = self.db.Productos.find()
        listaProductos = []
        for s in productos:
            listaProductos.append({"codigoBase":s["codigoBase"], "nombre":s["nombre"], "existencia":s["existencia"], "precios":s["precios"]})
        if len(listaProductos) > 0:
            resp["estatus"]="ok"
            resp["mensaje"]="Lista de productos"
            resp["productos"]=listaProductos
        else:
            resp["estatus"]="error"
            resp["mensaje"]="No hay productos registrados"
        return resp
    
    def obtenerFotosProductos(self):
        resp={"estatus":"", "mensaje":""}
        productos = self.db.Productos.find()
        listaProductos = []
        for s in productos:
            image_base64 = base64.b64encode(s['foto']).decode('utf-8')
            listaProductos.append({"codigoBase":s["codigoBase"], "foto":image_base64})
        if len(listaProductos) > 0:
            resp["estatus"]="ok"
            resp["mensaje"]="Lista de productos"
            resp["productos"]=listaProductos
        else:
            resp["estatus"]="error"
            resp["mensaje"]="No hay productos registrados"
        return resp