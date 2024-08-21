from pymongo import MongoClient

class Conexion():
    def __init__(self, db_name):
        self.cliente = MongoClient("mongodb+srv://apbarajas658:32GeaC79hqdZNTbf@cluster0.6f3klmh.mongodb.net/")
        self.db = self.cliente[db_name]

    def registrarMarca(self, data):
        resp = {"estatus":"","mensaje":""}
        marca=self.db.Marcas.find_one({"nombre":data["nombre"]})
        if marca:
            resp["estatus"]="error"
            resp["mensaje"]="La marca ya existe"
        else:
            self.db.Marcas.insert_one(data)
            resp["estatus"]="ok"
            resp["mensaje"]="Marca registrada"
        return resp
    
    def obtenerMarcas(self):
        resp={"estatus":"", "mensaje":""}
        marcas = self.db.Marcas.find()
        listaMarcas = []
        for s in marcas:
            listaMarcas.append({"idMarca":s["idMarca"], "nombre":s["nombre"]})
        if len(listaMarcas) > 0:
            resp["estatus"]="ok"
            resp["mensaje"]="Lista de marcas"
            resp["marcas"]=listaMarcas
        else:
            resp["estatus"]="error"
            resp["mensaje"]="No hay marcas registradas"
        return resp
    
    def editarMarca(self, data):
        resp = {"estatus":"","mensaje":""}
        marca=self.db.Marcas.find_one({"idMarca":data["idMarca"]})
        if marca:
            self.db.Marcas.update_one({"idMarca":data["idMarca"]},{"$set":data})
            resp["estatus"]="ok"
            resp["mensaje"]="Marca actualizada"
        else:
            resp["estatus"]="error"
            resp["mensaje"]="Marca no encontrada"
        return resp
    
    def eliminarMarca(self, idMarca):
        resp = {"estatus":"","mensaje":""}
        marca=self.db.Marcas.find_one({"idMarca":idMarca})
        if marca:
            self.db.Marcas.delete_one({"idMarca":idMarca})
            resp["estatus"]="ok"
            resp["mensaje"]="Marca eliminada"
        else:
            resp["estatus"]="error"
            resp["mensaje"]="Marca no encontrada"
        return resp
    
    def obtenerUltimoIdM(self):
        resp = {"estatus":"","mensaje":""}
        marcas = self.db.Marcas.find().sort([("idMarca", -1)]).limit(1)
        for s in marcas:
            resp["estatus"]="ok"
            resp["mensaje"]="Ultimo id"
            resp["idMarca"]=s["idMarca"]
        return resp