from pymongo import MongoClient
from bson import ObjectId
from bson.binary import Binary
import base64
from pymongo.errors import DuplicateKeyError

class Conexion():
    def __init__(self, db_name):
        self.cliente = MongoClient("mongodb+srv://sipsasoluciones:sLHaml3BAWlERcoP@cluster0.idzpxoq.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
        # self.cliente = MongoClient("mongodb+srv://apbarajas658:32GeaC79hqdZNTbf@cluster0.6f3klmh.mongodb.net/")
        self.db = self.cliente[db_name]
    
    def registrarCliente(self, data):
        resp = {"estatus":"","mensaje":""}
        try:
            image_binary = base64.b64decode(data['foto'])
            data['foto'] = Binary(image_binary)
            self.db.Clientes.insert_one(data)
            resp["estatus"]="ok"
            resp["mensaje"]="Cliente registrado"
        except DuplicateKeyError:
            resp["estatus"]="error"
            resp["mensaje"]="El cliente ya existe"
        return resp
    
    def obtenerClientes(self):
        resp={"estatus":"", "mensaje":""}
        clientes = self.db.Clientes.find()
        listaClientes = []
        for s in clientes:
            image_base64 = base64.b64encode(s['foto']).decode('utf-8')
            listaClientes.append({"_id":str(s["_id"]), "nombre":s["nombre"], "apPaterno":s["apPaterno"], "apMaterno":s["apMaterno"], "foto":"", "telMovil":s["telMovil"], "email":s["email"]})
        if len(listaClientes) > 0:
            resp["estatus"]="ok"
            resp["mensaje"]="Lista de clientes"
            resp["clientes"]=listaClientes
        else:
            resp["estatus"]="error"
            resp["mensaje"]="No hay clientes registrados"
        return resp
    
    def obtenerCliente(self, id):
        resp={"estatus":"", "mensaje":""}
        cliente = self.db.Clientes.find_one({"_id":ObjectId(id)})
        if cliente:
            image_base64 = base64.b64encode(cliente['foto']).decode('utf-8')
            resp["estatus"]="ok"
            resp["mensaje"]="Cliente encontrado"
            resp["cliente"]={"_id":str(cliente["_id"]), "tipoPersona":cliente["tipoPersona"],"nombre":cliente["nombre"], "apPaterno":cliente["apPaterno"], "apMaterno":cliente["apMaterno"], "foto":image_base64, "telMovil":cliente["telMovil"], "email":cliente["email"], "curp":cliente["curp"], "nombreComercial":cliente["nombreComercial"],"rfc":cliente["rfc"], "ctaBancaria":cliente["ctaBancaria"], "banco":cliente["banco"],"domicilios":cliente["domicilios"]}
        else:
            resp["estatus"]="error"
            resp["mensaje"]="Cliente no encontrado"
        return resp
    
    def obtenerClienteNombre(self, data):
        resp = {"estatus": "", "mensaje": ""}
        cliente = self.db.Clientes.find_one({"nombre": data["nombre"]})
        if cliente:
            image_base64 = base64.b64encode(cliente['foto']).decode('utf-8')
            resp["estatus"] = "ok"
            resp["mensaje"] = "Cliente encontrado"
            resp["cliente"] = {
                "_id": str(cliente["_id"]),
                "tipoPersona": cliente["tipoPersona"],
                "nombre": cliente["nombre"],
                "apPaterno": cliente["apPaterno"],
                "apMaterno": cliente["apMaterno"],
                "telMovil": cliente["telMovil"],
                "email": cliente["email"],
                "curp": cliente["curp"],
                "nombreComercial": cliente["nombreComercial"],
                "rfc": cliente["rfc"],
                "ctaBancaria": cliente["ctaBancaria"],
                "banco": cliente["banco"],
                "domicilios": cliente["domicilios"]
            }
        else:
            resp["estatus"] = "error"
            resp["mensaje"] = "Cliente no encontrado"
        return resp
    
    def obtenerClientesVenta(self):
        resp={"estatus":"", "mensaje":""}
        clientes = self.db.Clientes.find()
        listaClientes = []
        for s in clientes:
            listaClientes.append({"_id":str(s["_id"]), "nombre":s["nombre"], "apPaterno":s["apPaterno"], "apMaterno":s["apMaterno"], "domicilios":s["domicilios"], "telMovil":s["telMovil"]})
        if len(listaClientes) > 0:
            resp["estatus"]="ok"
            resp["mensaje"]="Lista de clientes"
            resp["clientes"]=listaClientes
        else:
            resp["estatus"]="error"
            resp["mensaje"]="No hay clientes registrados"
        return resp
    
    def editarCliente(self, data):
        resp = {"estatus":"","mensaje":""}
        cliente=self.db.Clientes.find_one({"_id":ObjectId(data["_id"])})
        if cliente:
            if 'foto' in data:
                image_binary = base64.b64decode(data['foto'])
                data['foto'] = Binary(image_binary)
            # Remove the _id key from data
            data.pop('_id', None)
            self.db.Clientes.update_one({"_id":ObjectId(cliente["_id"])},{"$set":data})
            resp["estatus"]="ok"
            resp["mensaje"]="Cliente actualizado"
        else:
            resp["estatus"]="error"
            resp["mensaje"]="Cliente no encontrado"
        return resp
    
    def eliminarCliente(self, id):
        resp = {"estatus":"","mensaje":""}
        cliente=self.db.Clientes.find_one({"_id":ObjectId(id)})
        if cliente:
            self.db.Clientes.delete_one({"_id":ObjectId(id)})
            resp["estatus"]="ok"
            resp["mensaje"]="Cliente eliminado"
        else:
            resp["estatus"]="error"
            resp["mensaje"]="Cliente no encontrado"
        return resp
    