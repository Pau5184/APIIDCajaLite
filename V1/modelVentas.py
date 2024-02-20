from pymongo import MongoClient
from bson import ObjectId
from bson.binary import Binary
import base64

class Conexion():
    def __init__(self):
        self.cliente = MongoClient("mongodb+srv://apbarajas658:32GeaC79hqdZNTbf@cluster0.6f3klmh.mongodb.net/")
        self.db = self.cliente.IDCajaLite

    def registrarVenta(self, data):
        resp = {"estatus":"","mensaje":""}
        try:
            data["cliente"]=ObjectId(data["cliente"])
            data["cajero"]=ObjectId(data["cajero"])
            self.db.Ventas.insert_one(data)
            for producto in data['productos']:
                self.db.Productos.update_one(
                    {'codigoBase': producto['producto']},
                    {'$inc': {'existencia': -producto['cantidad']}}
                )
            resp["estatus"]="ok"
            resp["mensaje"]="Venta registrada"
        except Exception as e:
            resp["estatus"]="error"
            resp["mensaje"]=str(e)
        return resp
    
    def obtenerVentas(self):
        resp={"estatus":"", "mensaje":""}
        ventas = self.db.Ventas.find()
        listaVentas = []
        for s in ventas:
            cliente=self.db.Clientes.find_one({"_id":(s["cliente"])})
            s["cliente"]=cliente["nombre"] + (" "+cliente["apPaterno"] if 'apPaterno' in cliente else "")+(" "+cliente["apMaterno"] if 'apMaterno' in cliente else "")
            usuario=self.db.Usuarios.find_one({"_id":(s["cajero"])})
            s["cajero"]=usuario["nombre"]+(" "+usuario["apPaterno"] if 'apPaterno' in usuario else "")+(" "+usuario["apMaterno"] if 'apMaterno' in usuario else "")
            listaVentas.append({"idVenta":str(s["_id"]), "fechaVenta":s["fechaVenta"], "horaVenta":s["horaVenta"], "cliente":s["cliente"], "cajero":s["cajero"], "pagadoEfectivo":s["pagadoEfectivo"], "pagadoTarjeta":s["pagadoTarjeta"], "pagadoTrans":s["pagadoTrans"], "total":s["total"]})
        if len(listaVentas) > 0:
            resp["estatus"]="ok"
            resp["mensaje"]="Lista de ventas"
            resp["ventas"]=listaVentas
        else:
            resp["estatus"]="error"
            resp["mensaje"]="No hay ventas registradas"
        return resp
    
    ##Obtener el id de una venta por fecha, hora, total, cliente y cajero
    def obtenerIdVenta(self, data):
        resp = {"estatus":"","mensaje":""}
        venta = self.db.Ventas.find_one({"fechaVenta":data["fechaVenta"],"horaVenta":data["horaVenta"],"total":data["total"],"cliente":ObjectId(data["cliente"]),"cajero":ObjectId(data["cajero"])})
        if venta:
            resp["estatus"]="ok"
            resp["mensaje"]="Venta encontrada"
            resp["idVenta"]=str(venta["_id"])
        else:
            resp["estatus"]="error"
            resp["mensaje"]="Venta no encontrada"
        return resp
    
    def obtenerTiquet(self, id):
        resp = {"estatus":"","mensaje":""}
        venta = self.db.Ventas.find_one({"_id":ObjectId(id)})
        if venta:
            if 'tiquet' in venta:
                resp["estatus"]="ok"
                resp["mensaje"]="Tiquet encontrado"
                resp["tiquet"]=base64.b64encode(venta["tiquet"]).decode('utf-8')
            else:
                resp["estatus"]="error"
                resp["mensaje"]="Tiquet no encontrado"
        else:
            resp["estatus"]="error"
            resp["mensaje"]="Venta no encontrada"
        return resp
    
    def editarVenta(self, data):
        resp = {"estatus":"","mensaje":""}
        venta=self.db.Ventas.find_one({"_id":ObjectId(data["_id"])})
        if venta:
            if 'tiquet' in data:
                image_binary = base64.b64decode(data['tiquet'])
                data['tiquet'] = Binary(image_binary)
            # Remove the _id key from data
            data.pop('_id', None)
            self.db.Ventas.update_one({"_id":ObjectId(venta["_id"])},{"$set":data})
            resp["estatus"]="ok"
            resp["mensaje"]="Venta actualizada"
        else:
            resp["estatus"]="error"
            resp["mensaje"]="Venta no encontrada"
        return resp

    