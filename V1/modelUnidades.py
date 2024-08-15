from pymongo import MongoClient

class Conexion():
    def __init__(self):
        self.cliente = MongoClient("mongodb+srv://apbarajas658:32GeaC79hqdZNTbf@cluster0.6f3klmh.mongodb.net/")
        self.db = self.cliente.IDCajaLite

    def registrarUnidad(self, data):
        resp = {"estatus":"","mensaje":""}
        unidad=self.db.UnidadesMedida.find_one({"nombre":data["nombre"]})
        if unidad:
            resp["estatus"]="error"
            resp["mensaje"]="La unidad ya existe"
        else:
            self.db.Unidades.insert_one(data)
            resp["estatus"]="ok"
            resp["mensaje"]="Unidad registrada"
        return resp
    
    def obtenerUnidades(self):
        resp={"estatus":"", "mensaje":""}
        unidades = self.db.UnidadesMedida.find()
        listaUnidades = []
        for s in unidades:
            listaUnidades.append({"idUnidad":s["idUnidad"], "nombre":s["nombre"]})
        if len(listaUnidades) > 0:
            resp["estatus"]="ok"
            resp["mensaje"]="Lista de unidades"
            resp["unidades"]=listaUnidades
        else:
            resp["estatus"]="error"
            resp["mensaje"]="No hay unidades registradas"
        return resp
    
    def editarUnidad(self, data):
        resp = {"estatus":"","mensaje":""}
        unidad=self.db.UnidadesMedida.find_one({"idUnidad":data["idUnidad"]})
        if unidad:
            self.db.UnidadesMedida.update_one({"idUnidad":data["idUnidad"]},{"$set":data})
            resp["estatus"]="ok"
            resp["mensaje"]="Unidad actualizada"
        else:
            resp["estatus"]="error"
            resp["mensaje"]="Unidad no encontrada"
        return resp
    
    def eliminarUnidad(self, idUnidad):
        resp = {"estatus":"","mensaje":""}
        unidad=self.db.UnidadesMedida.find_one({"idUnidad":idUnidad})
        if unidad:
            self.db.UnidadesMedida.delete_one({"idUnidad":idUnidad})
            resp["estatus"]="ok"
            resp["mensaje"]="Unidad eliminada"
        else:
            resp["estatus"]="error"
            resp["mensaje"]="Unidad no encontrada"
        return resp
    
    def obtenerUltimoIdU(self):
        resp = {"estatus":"","mensaje":""}
        ultimoId = self.db.UnidadesMedida.find().sort([("idUnidad",-1)]).limit(1)
        for s in ultimoId:
            resp["ultimoId"]=s["idUnidad"]
        return resp