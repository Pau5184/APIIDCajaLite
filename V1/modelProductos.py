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
            image_base64 = base64.b64encode(s['foto']).decode('utf-8')
            listaProductos.append({"codigoBase":s["codigoBase"], "nombre":s["nombre"], "foto":image_base64, "existencia":s["existencia"], "precios":s["precios"], "unidadBase":s["unidadBase"], "unidadCompra":s["unidadCompra"]})
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
            resp["mensaje"]="Lista de fotos"
            resp["fotos"]=listaProductos
        else:
            resp["estatus"]="error"
            resp["mensaje"]="No hay productos registrados"
        return resp
    
    def obtenerProducto(self, codigoBase):
        resp={"estatus":"", "mensaje":""}
        producto = self.db.Productos.find_one({"codigoBase":codigoBase})
        if producto:
            image_base64 = base64.b64encode(producto['foto']).decode('utf-8')
            resp["estatus"]="ok"
            resp["mensaje"]="Producto encontrado"
            resp["producto"]={"codigoBase":producto["codigoBase"], "nombre":producto["nombre"], "descripcion":producto["descripcion"],"foto":image_base64, "unidadBase":producto["unidadBase"], "unidadCompra":producto["unidadCompra"], "factorConversion":producto["factorConversion"],"existencia":producto["existencia"], "proveedor":producto["proveedor"], "estatus":producto["estatus"], "minimoVender":producto["minimoVender"], "marca":producto["marca"], "linea":producto["linea"], "ancho":producto["ancho"], "alto":producto["alto"], "largo":producto["largo"], "volumen":producto["volumen"], "impuestos":producto["impuestos"], "precios":producto["precios"]}
        else:
            resp["estatus"]="error"
            resp["mensaje"]="Producto no encontrado"
        return resp
    
    def editarProducto(self, data):
        resp = {"estatus":"","mensaje":""}
        producto=self.db.Productos.find_one({"codigoBase":data["codigoBase"]})
        if producto:
            if 'foto' in data:
                image_binary = base64.b64decode(data['foto'])
                data['foto'] = Binary(image_binary)
            self.db.Productos.update_one({"codigoBase":data["codigoBase"]},{"$set":data})
            resp["estatus"]="ok"
            resp["mensaje"]="Producto actualizado"
        else:
            resp["estatus"]="error"
            resp["mensaje"]="Producto no encontrado"
        return resp
    
    def eliminarProducto(self, codigoBase):
        resp = {"estatus":"","mensaje":""}
        producto=self.db.Productos.find_one({"codigoBase":codigoBase})
        if producto:
            self.db.Productos.delete_one({"codigoBase":codigoBase})
            resp["estatus"]="ok"
            resp["mensaje"]="Producto eliminado"
        else:
            resp["estatus"]="error"
            resp["mensaje"]="Producto no encontrado"
        return resp
    
    def obtenerProductosVenta(self):
        resp={"estatus":"", "mensaje":""}
        productos = self.db.Productos.find()
        listaProductos = []
        for s in productos:
            # Check if the precios array is not empty
            if s['precios']:
                image_base64 = base64.b64encode(s['foto']).decode('utf-8')
                listaProductos.append({
                    "codigoBase":s["codigoBase"], 
                    "nombre":s["nombre"], 
                    "foto":image_base64, 
                    "existencia":s["existencia"], 
                    "precio":s["precios"][0]["total"],  # Only include the total of the first precio
                    "unidadBase":s["unidadBase"]
                })
        if len(listaProductos) > 0:
            resp["estatus"]="ok"
            resp["mensaje"]="Lista de productos"
            resp["productos"]=listaProductos
        else:
            resp["estatus"]="error"
            resp["mensaje"]="No hay productos registrados"
        return resp