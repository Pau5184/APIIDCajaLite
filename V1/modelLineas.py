from pymongo import MongoClient

class Conexion():
    def __init__(self, db_name):
        self.cliente = MongoClient("mongodb+srv://apbarajas658:32GeaC79hqdZNTbf@cluster0.6f3klmh.mongodb.net/")
        self.db = self.cliente[db_name]
    
    def registrarLinea(self, data):
        resp = {"estatus":"","mensaje":""}
        linea=self.db.Lineas.find_one({"nombre":data["nombre"]})
        if linea:
            resp["estatus"]="error"
            resp["mensaje"]="La linea ya existe"
        else:
            self.db.Lineas.insert_one(data)
            resp["estatus"]="ok"
            resp["mensaje"]="Linea registrada"
        return resp
    
    def obtenerLineas(self):
        resp={"estatus":"", "mensaje":""}
        lineas = self.db.Lineas.find()
        listaLineas = []
        for s in lineas:
            listaLineas.append({"idLinea":s["idLinea"], "nombre":s["nombre"]})
        if len(listaLineas) > 0:
            resp["estatus"]="ok"
            resp["mensaje"]="Lista de lineas"
            resp["lineas"]=listaLineas
        else:
            resp["estatus"]="error"
            resp["mensaje"]="No hay lineas registradas"
        return resp
    
    def editarLinea(self, data):
        resp = {"estatus":"","mensaje":""}
        linea=self.db.Lineas.find_one({"idLinea":data["idLinea"]})
        if linea:
            self.db.Lineas.update_one({"idLinea":data["idLinea"]},{"$set":data})
            resp["estatus"]="ok"
            resp["mensaje"]="Linea actualizada"
        else:
            resp["estatus"]="error"
            resp["mensaje"]="Linea no encontrada"
        return resp
    
    def eliminarLinea(self, idLinea):
        resp = {"estatus":"","mensaje":""}
        linea=self.db.Lineas.find_one({"idLinea":idLinea})
        if linea:
            self.db.Lineas.delete_one({"idLinea":idLinea})
            resp["estatus"]="ok"
            resp["mensaje"]="Linea eliminada"
        else:
            resp["estatus"]="error"
            resp["mensaje"]="Linea no encontrada"
        return resp
    
    def obtenerUltimoIdL(self):
        resp = {"estatus":"","mensaje":""}
        lineas = self.db.Lineas.find().sort([("idLinea",-1)]).limit(1)
        for s in lineas:
            resp["estatus"]="ok"
            resp["mensaje"]="Ultimo id"
            resp["ultimoId"]=s["idLinea"]
        return resp