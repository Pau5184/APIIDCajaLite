from pymongo import MongoClient
from bson import ObjectId
from bson.binary import Binary
import base64

class Conexion():
    def __init__(self):
        self.cliente = MongoClient("mongodb+srv://apbarajas658:32GeaC79hqdZNTbf@cluster0.6f3klmh.mongodb.net/")
        self.db = self.cliente.IDCajaLite

    def obtenerEmpresa(self):
        resp={"estatus":"", "mensaje":""}
        empresa = self.db.Empresa.find_one()
        if empresa:
            image_base64 = base64.b64encode(empresa['logo']).decode('utf-8')
            resp["estatus"]="ok"
            resp["mensaje"]="Datos de la empresa"
            resp["empresa"]={"nombre":empresa["nombre"], "logo":image_base64, "direccion":empresa["direccion"], "telefono":empresa["telefono"]}
        else:
            resp["estatus"]="error"
            resp["mensaje"]="No hay datos de la empresa"
        return resp
    
    def editarEmpresa(self, data):
        resp = {"estatus":"","mensaje":""}
        empresa=self.db.Empresa.find_one()
        if empresa:
            if 'logo' in data:
                image_binary = base64.b64decode(data['logo'])
                data['logo'] = Binary(image_binary)
            self.db.Empresa.update_one({},{"$set":data})
            resp["estatus"]="ok"
            resp["mensaje"]="Datos de la empresa actualizados"
        else:
            resp["estatus"]="error"
            resp["mensaje"]="No hay datos de la empresa"
        return resp