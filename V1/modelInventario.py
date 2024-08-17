from pymongo import MongoClient
from bson import ObjectId
from bson.binary import Binary
from datetime import datetime
import base64

class Conexion():
    def __init__(self):
        self.cliente = MongoClient("mongodb+srv://apbarajas658:32GeaC79hqdZNTbf@cluster0.6f3klmh.mongodb.net/")
        self.db = self.cliente.IDCajaLite
    
    def registrarInventario(self, data):
        resp = {"estatus":"","mensaje":""}
        try:
            data["usuario"]=ObjectId(data["usuario"])
            self.db.Inventario.insert_one(data)
            for producto in data['productos']:
                if data['concepto'] in ["ENTRADA DE MERCANCIA"]:
                    self.db.Productos.update_one(
                        {'codigoBase': producto['producto']},
                        {'$inc': {'existencia': producto['cantidad']}}
                    )
                else:
                    self.db.Productos.update_one(
                        {'codigoBase': producto['producto']},
                        {'$inc': {'existencia': -producto['cantidad']}}
                    )
            resp["estatus"]="ok"
            resp["mensaje"]="Producto registrado"
        except Exception as e:
            resp["estatus"]="error"
            resp["mensaje"]=str(e)
        return resp
    
    ##Obtener lista de inventarios. Datos a obtener: _id, concepto, fecha, totalUnidades
    def obtenerInventarios(self, data):
        start_date_str = data["startdate"];
        end_date_str = data["enddate"];
        resp = {"estatus": "", "mensaje": ""}
        # Convert start and end dates to datetime objects
        try:
            start_date = datetime.strptime(start_date_str, "%d/%m/%Y")
        except ValueError:
            start_date = datetime.strptime(start_date_str, "%m/%d/%Y")
        
        try:
            end_date = datetime.strptime(end_date_str, "%d/%m/%Y")
        except ValueError:
            end_date = datetime.strptime(end_date_str, "%m/%d/%Y")

        # Ensure end_date is at the end of the day
        end_date = end_date.replace(hour=23, minute=59, second=59)

        inventarios = self.db.Inventario.find()

        listaInventarios = []
        for s in inventarios:
            # Attempt to parse the fecha field
            try:
                fecha_inventario = datetime.strptime(s["fecha"], "%d/%m/%Y")
            except ValueError:
                fecha_inventario = datetime.strptime(s["fecha"], "%m/%d/%Y")
            
            # Include the inventory if its fecha is within the specified range
            if start_date <= fecha_inventario <= end_date:
                listaInventarios.append({
                    "_id": str(s["_id"]),
                    "concepto": s["concepto"],
                    "fecha": s["fecha"],
                    "totalUnidades": s["totalUnidades"],
                    "hora": s["hora"]
                })

        # Helper function to parse date
        def parse_datetime(date_str, time_str):
            try:
                return datetime.strptime(date_str + " " + time_str, "%d/%m/%Y %H:%M")
            except ValueError:
                return datetime.strptime(date_str + " " + time_str, "%m/%d/%Y %H:$M")

        # Sort the list of inventories by date
        listaInventarios.sort(key=lambda x: parse_datetime(x["fecha"], x["hora"]), reverse= True)

        if len(listaInventarios) > 0:
            resp["estatus"] = "ok"
            resp["mensaje"] = "Lista de inventarios"
            resp["inventarios"] = listaInventarios
        else:
            resp["estatus"] = "error"
            resp["mensaje"] = "No hay inventarios registrados en el rango de fechas proporcionado"
        
        return resp
    
    ##Obtener un inventario por id. Datos a obtener: _id, concepto, almacen, usuario (obtener el nombre del usuario ya que viene el id), estatus, fecha, totalUnidades, productos (id, producto (obtener el nombre del producto), cantidad, costoCompra), partidas, total
    def obtenerInventario(self, id):
        resp={"estatus":"", "mensaje":""}
        inventario = self.db.Inventario.find_one({"_id":ObjectId(id)})
        if inventario:
            usuario=self.db.Usuarios.find_one({"_id":(inventario["usuario"])})
            listaProductos = []
            for s in inventario["productos"]:
                producto=self.db.Productos.find_one({"codigoBase":(s["producto"])})
                listaProductos.append({"codigoBase":producto["codigoBase"], "producto":producto["nombre"], "cantidad":s["cantidad"], "costoCompra":s["costoCompra"]})
            resp["estatus"]="ok"
            resp["mensaje"]="Inventario encontrado"
            resp["inventario"]={"_id":str(inventario["_id"]), "concepto":inventario["concepto"], "almacen":inventario["almacen"], "usuario":usuario["nombre"], "estatus":inventario["estatus"], "fecha":inventario["fecha"], "hora":inventario["hora"], "totalUnidades":inventario["totalUnidades"], "productos":listaProductos, "partidas":inventario["partidas"], "total":inventario["total"]}
        else:
            resp["estatus"]="error"
            resp["mensaje"]="Inventario no encontrado"
        return resp