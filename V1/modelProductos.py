from pymongo import MongoClient
from bson import ObjectId
from bson.binary import Binary
import base64

class Conexion():
    def __init__(self, db_name):
        self.cliente = MongoClient("mongodb+srv://sipsasoluciones:sLHaml3BAWlERcoP@cluster0.idzpxoq.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
        # self.cliente = MongoClient("mongodb+srv://apbarajas658:32GeaC79hqdZNTbf@cluster0.6f3klmh.mongodb.net/")
        self.db = self.cliente[db_name]
        
    def registrarProducto(self, data):
        resp = {"estatus": "", "mensaje": ""}
        try:
            producto = self.db.Productos.find_one({"codigoBase": data["codigoBase"]})
            if producto:
                resp["estatus"] = "error"
                resp["mensaje"] = "Error. Este producto ya existe. Inténtelo de nuevo"
            else:
                image_binary = base64.b64decode(data['foto'])
                data['foto'] = Binary(image_binary)
                
                if data["unidadBase"]:
                    data["unidadBase"] = ObjectId(data["unidadBase"])
                
                if data["unidadCompra"]:
                    data["unidadCompra"] = ObjectId(data["unidadCompra"])
                
                if data["marca"]:
                    data["marca"] = ObjectId(data["marca"])

                if data["linea"]:
                    data["linea"] = ObjectId(data["linea"])
                
                self.db.Productos.insert_one(data)
                resp["estatus"] = "ok"
                resp["mensaje"] = "Producto registrado"
        except Exception as e:
            resp["estatus"] = "error"
            resp["mensaje"] = str(e)
        return resp
    
    def obtenerProductos(self):
        resp = {"estatus": "", "mensaje": ""}
        productos = self.db.Productos.find()
        listaProductos = []
        
        for s in productos:
            image_base64 = base64.b64encode(s['foto']).decode('utf-8')
            
            # Look up unidadBase in UnidadesMedida collection
            unidad_base_nombre = ""
            if s["unidadBase"]:
                unidad_base = self.db.UnidadesMedida.find_one({"_id": ObjectId(s["unidadBase"])})
                if unidad_base:
                    unidad_base_nombre = unidad_base.get("nombre")
            
            # Look up unidadCompra in UnidadesMedida collection
            unidad_compra_nombre = ""
            if s["unidadCompra"]:
                unidad_compra = self.db.UnidadesMedida.find_one({"_id": ObjectId(s["unidadCompra"])})
                if unidad_compra:
                    unidad_compra_nombre = unidad_compra.get("nombre")
            
            listaProductos.append({
                "codigoBase": s["codigoBase"],
                "nombre": s["nombre"],
                "existencia": s["existencia"],
                "precios": s["precios"],
                "unidadBase": unidad_base_nombre,
                "unidadCompra": unidad_compra_nombre,
                "costoCompra": s["costoCompra"],
                "fechaUltimaCompra": s["fechaUltimaCompra"],
                "foto": image_base64,
                "factorConversion": s["factorConversion"]
            })
        
        if len(listaProductos) > 0:
            resp["estatus"] = "ok"
            resp["mensaje"] = "Lista de productos"
            resp["productos"] = listaProductos
        else:
            resp["estatus"] = "error"
            resp["mensaje"] = "No hay productos registrados"
        
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
        resp = {"estatus": "", "mensaje": ""}
        try:
            producto = self.db.Productos.find_one({"codigoBase": codigoBase})
            
            if producto:
                image_base64 = base64.b64encode(producto['foto']).decode('utf-8')
                
                # Look up unidadBase in UnidadesMedida collection
                unidad_base_nombre = ""
                unidad_base_id = ""
                if producto["unidadBase"]:
                    unidad_base = self.db.UnidadesMedida.find_one({"_id": ObjectId(producto["unidadBase"])})
                    if unidad_base:
                        unidad_base_nombre = unidad_base.get("nombre")
                        unidad_base_id = str(producto["unidadBase"])
                
                # Look up unidadCompra in UnidadesMedida collection
                unidad_compra_nombre = ""
                unidad_compra_id = ""
                if producto["unidadCompra"]:
                    unidad_compra = self.db.UnidadesMedida.find_one({"_id": ObjectId(producto["unidadCompra"])})
                    if unidad_compra:
                        unidad_compra_nombre = unidad_compra.get("nombre")
                        unidad_compra_id = str(producto["unidadCompra"])
                
                # Look up marca in Marcas collection
                marca_nombre = ""
                marca_id = ""
                if producto["marca"]:
                    marca = self.db.Marcas.find_one({"_id": ObjectId(producto["marca"])})
                    if marca:
                        marca_nombre = marca.get("nombre")
                        marca_id = str(producto["marca"])
                
                # Look up linea in Lineas collection
                linea_nombre = ""
                linea_id = ""
                if producto["linea"]:
                    linea = self.db.Lineas.find_one({"_id": ObjectId(producto["linea"])})
                    if linea:
                        linea_nombre = linea.get("nombre")
                        linea_id = str(producto["linea"])
                
                resp["estatus"] = "ok"
                resp["mensaje"] = "Producto encontrado"
                resp["producto"] = {
                    "codigoBase": producto["codigoBase"],
                    "nombre": producto["nombre"],
                    "descripcion": producto["descripcion"],
                    "unidadBase": unidad_base_nombre,
                    "unidadBaseId": unidad_base_id,
                    "unidadCompra": unidad_compra_nombre,
                    "unidadCompraId": unidad_compra_id,
                    "factorConversion": producto["factorConversion"],
                    "existencia": producto["existencia"],
                    "proveedor": producto["proveedor"],
                    "estatus": producto["estatus"],
                    "minimoVender": producto["minimoVender"],
                    "linea": linea_nombre,
                    "lineaId": linea_id,
                    "marca": marca_nombre,
                    "marcaId": marca_id,
                    "ancho": producto["ancho"],
                    "alto": producto["alto"],
                    "largo": producto["largo"],
                    "volumen": producto["volumen"],
                    "precios": producto["precios"],
                    "costoCompra": producto["costoCompra"],
                    "fechaUltimaCompra": producto["fechaUltimaCompra"],
                    "foto": image_base64
                }
            else:
                resp["estatus"] = "error"
                resp["mensaje"] = "Producto no encontrado"
        except PyMongoError as e:
            resp["estatus"] = "error"
            resp["mensaje"] = f"Database error: {str(e)}"
        except Exception as e:
            resp["estatus"] = "error"
            resp["mensaje"] = f"Unexpected error: {str(e)}"
        
        return resp
    
    def editarProducto(self, data):
        resp = {"estatus":"","mensaje":""}
        try:
            producto=self.db.Productos.find_one({"codigoBase":data["codigoBase"]})
            if producto:
                if 'foto' in data:
                    image_binary = base64.b64decode(data['foto'])
                    data['foto'] = Binary(image_binary)

                # Look up unidadBase and unidadCompra in UnidadesMedida collection
                if 'unidadBase' in data and data["unidadBase"]:
                    try:
                        data["unidadBase"] = ObjectId(data["unidadBase"])
                    except Exception as e:
                        data["unidadBase"] = ""

                if 'unidadCompra' in data and data["unidadCompra"]:
                    try:
                        data["unidadCompra"] = ObjectId(data["unidadCompra"])
                    except Exception as e:
                        data["unidadCompra"] = ""
                
                # Look up marca in Marcas collection
                if 'marca' in data and data["marca"]:
                    try:
                        data["marca"] = ObjectId(data["marca"])
                    except Exception as e:
                        data["marca"] = ""
                
                # Look up linea in Lineas collection
                if 'linea' in data and data["linea"]:
                    try:
                        data["linea"] = ObjectId(data["linea"])
                    except Exception as e:
                        data["linea"] = ""
                
                self.db.Productos.update_one({"codigoBase":data["codigoBase"]},{"$set":data})
                resp["estatus"]="ok"
                resp["mensaje"]="Producto actualizado"
            else:
                resp["estatus"]="error"
                resp["mensaje"]="Producto no encontrado"
        except Exception as e:
            resp["estatus"]="error"
            resp["mensaje"]=str
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
                # Look up unidadBase in UnidadesMedida collection
                unidad_base_nombre = ""
                if s["unidadBase"]:
                    unidad_base = self.db.UnidadesMedida.find_one({"_id": ObjectId(s["unidadBase"])})
                    if unidad_base:
                        unidad_base_nombre = unidad_base.get("nombre")

                listaProductos.append({
                    "codigoBase":s["codigoBase"], 
                    "nombre":s["nombre"], 
                    "existencia":s["existencia"], 
                    "precios":s["precios"],  # Only include the total of the first precio
                    "precioSeleccionado":s["precios"][0],
                    "unidadBase":unidad_base_nombre,
                    "foto":image_base64
                })
        if len(listaProductos) > 0:
            resp["estatus"]="ok"
            resp["mensaje"]="Lista de productos"
            resp["productos"]=listaProductos
        else:
            resp["estatus"]="error"
            resp["mensaje"]="No hay productos registrados"
        return resp