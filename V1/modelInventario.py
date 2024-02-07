from pymongo import MongoClient
from bson import ObjectId
from bson.binary import Binary
import base64

class Conexion():
    def __init__(self):
        self.cliente = MongoClient("mongodb+srv://apbarajas658:32GeaC79hqdZNTbf@cluster0.6f3klmh.mongodb.net/")
        self.db = self.cliente.IDCajaLite
    
    def registrarInventario(self, data):
        resp = {"estatus":"","mensaje":""}
        try:
            self.db.Inventario.insert_one(data)
            resp["estatus"]="ok"
            resp["mensaje"]="Producto registrado"
        except Exception as e:
            resp["estatus"]="error"
            resp["mensaje"]=str(e)
        return resp
    
    ##Obtener lista de inventarios. Datos a obtener: _id, concepto, fecha, totalUnidades
    def obtenerInventarios(self):
        resp={"estatus":"", "mensaje":""}
        inventarios = self.db.Inventario.find()
        listaInventarios = []
        for s in inventarios:
            listaInventarios.append({"_id":str(s["_id"]), "concepto":s["concepto"], "fecha":s["fecha"], "totalUnidades":s["totalUnidades"]})
        if len(listaInventarios) > 0:
            resp["estatus"]="ok"
            resp["mensaje"]="Lista de inventarios"
            resp["inventarios"]=listaInventarios
        else:
            resp["estatus"]="error"
            resp["mensaje"]="No hay inventarios registrados"
        return resp
    
    ##Obtener un inventario por id. Datos a obtener: _id, concepto, tipo, almacen, usuario (obtener el nombre del usuario ya que viene el id), estatus, fecha, totalUnidades, productos (id, producto (obtener el nombre del producto), cantidad, costoCompra), partidas, total
    def obtenerInventario(self, id):
        resp={"estatus":"", "mensaje":""}
        inventario = self.db.Inventario.find_one({"_id":ObjectId(id)})
        if inventario:
            usuario=self.db.Usuarios.find_one({"_id":ObjectId(inventario["usuario"])})
            listaProductos = []
            for s in inventario["productos"]:
                producto=self.db.Productos.find_one({"_id":ObjectId(s["producto"])})
                listaProductos.append({"codigoBase":producto["codigoBase"], "producto":producto["nombre"], "cantidad":s["cantidad"], "costoCompra":s["costoCompra"]})
            resp["estatus"]="ok"
            resp["mensaje"]="Inventario encontrado"
            resp["inventario"]={"_id":str(inventario["_id"]), "concepto":inventario["concepto"], "tipo":inventario["tipo"], "almacen":inventario["almacen"], "usuario":usuario["nombre"], "estatus":inventario["estatus"], "fecha":inventario["fecha"], "totalUnidades":inventario["totalUnidades"], "productos":listaProductos, "partidas":inventario["partidas"], "total":inventario["total"]}
        else:
            resp["estatus"]="error"
            resp["mensaje"]="Inventario no encontrado"
        return resp