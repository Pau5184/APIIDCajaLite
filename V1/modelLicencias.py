from pymongo import MongoClient
from bson import ObjectId
from bson.binary import Binary
from datetime import datetime
from dateutil.parser import parse

class Conexion():
    def __init__(self):
        self.cliente = MongoClient("mongodb+srv://sipsasoluciones:sLHaml3BAWlERcoP@cluster0.idzpxoq.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
        self.db = self.cliente.Licencias

    def registrarLicencia(self, data):
        resp = {"estatus": "", "mensaje": ""}
        try:
            # Convert fechaActivacion and fechaExpiracion to date type
            if "fechaActivacion" in data:
                data["fechaActivacion"] = datetime.fromisoformat(data["fechaActivacion"].replace("Z", "+00:00"))
            if "fechaExpiracion" in data:
                data["fechaExpiracion"] = datetime.fromisoformat(data["fechaExpiracion"].replace("Z", "+00:00"))
            
            self.db.Licencias.insert_one(data)
            resp["estatus"] = "ok"
            resp["mensaje"] = "Licencia registrada con éxito"
        except Exception as e:
            resp["estatus"] = "error"
            resp["mensaje"] = str(e)
        return resp
    
    #Validate license by device id number. Also validate fechaExpiracion is lower or equals than today's date (d/m/a)
    def validarLicencia(self, data):
        resp = {"estatus": "", "mensaje": ""}
        try:
            licencia = self.db.Licencias.find_one({"dispositivo": data["deviceId"]})
            if licencia:
                fechaExpiracion = licencia["fechaExpiracion"]
                activado = licencia["activado"]
                fechaActual = datetime.now()
                if activado:
                    if fechaExpiracion >= fechaActual:
                        resp["estatus"] = "ok"
                        resp["mensaje"] = "Licencia válida"
                    else:
                        resp["estatus"] = "error"
                        resp["mensaje"] = "Licencia expirada"
                else:
                    resp["estatus"] = "error"
                    resp["mensaje"] = "Licencia no activada"
            else:
                resp["estatus"] = "error"
                resp["mensaje"] = "No existe el dispositivo"
        except Exception as e:
            resp["estatus"] = "error"
            resp["mensaje"] = str(e)
        return resp
            