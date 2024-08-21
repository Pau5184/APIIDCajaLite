from flask import Blueprint, request
from V1.modelProductos import Conexion

productosBP = Blueprint('ProductosBP', __name__)

@productosBP.route('/registrarProducto', methods=['POST'])
def registrarProducto():
    data = request.get_json()
    db_name = request.args.get('db_name')
    if not db_name:
        return {"estatus": "error", "mensaje": "Database name is required"}, 400
    conn = Conexion(db_name)
    resp = conn.registrarProducto(data)
    return resp

@productosBP.route('/obtenerProductos', methods=['GET'])
def obtenerProductos():
    db_name = request.args.get('db_name')
    if not db_name:
        return {"estatus": "error", "mensaje": "Database name is required"}, 400
    conn = Conexion(db_name)
    resp = conn.obtenerProductos()
    return resp

@productosBP.route('/obtenerFotosProductos', methods=['GET'])
def obtenerFotosProductos():
    db_name = request.args.get('db_name')
    if not db_name:
        return {"estatus": "error", "mensaje": "Database name is required"}, 400
    conn = Conexion(db_name)
    resp = conn.obtenerFotosProductos()
    return resp

@productosBP.route('/obtenerProducto/<codigoBase>', methods=['GET'])
def obtenerProducto(codigoBase):
    db_name = request.args.get('db_name')
    if not db_name:
        return {"estatus": "error", "mensaje": "Database name is required"}, 400
    conn = Conexion(db_name)
    resp = conn.obtenerProducto(codigoBase)
    return resp

@productosBP.route('/obtenerProductosVenta', methods=['GET'])
def obtenerProductosVenta():
    db_name = request.args.get('db_name')
    if not db_name:
        return {"estatus": "error", "mensaje": "Database name is required"}, 400
    conn = Conexion(db_name)
    resp = conn.obtenerProductosVenta()
    return resp

#Editar producto
@productosBP.route('/editarProducto', methods=['PUT'])
def editarProducto():
    data = request.get_json()
    db_name = request.args.get('db_name')
    if not db_name:
        return {"estatus": "error", "mensaje": "Database name is required"}, 400
    conn = Conexion(db_name)
    resp = conn.editarProducto(data)
    return resp

#Eliminar producto
@productosBP.route('/eliminarProducto/<codigoBase>', methods=['DELETE'])
def eliminarProducto(codigoBase):
    db_name = request.args.get('db_name')
    if not db_name:
        return {"estatus": "error", "mensaje": "Database name is required"}, 400
    conn = Conexion(db_name)
    resp = conn.eliminarProducto(codigoBase)
    return resp