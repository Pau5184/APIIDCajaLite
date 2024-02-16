from flask import Blueprint, request
from V1.modelProductos import Conexion

productosBP = Blueprint('ProductosBP', __name__)

@productosBP.route('/registrarProducto', methods=['POST'])
def registrarProducto():
    data = request.get_json()
    conn = Conexion()
    resp = conn.registrarProducto(data)
    return resp

@productosBP.route('/obtenerProductos', methods=['GET'])
def obtenerProductos():
    conn = Conexion()
    resp = conn.obtenerProductos()
    return resp

@productosBP.route('/obtenerFotosProductos', methods=['GET'])
def obtenerFotosProductos():
    conn = Conexion()
    resp = conn.obtenerFotosProductos()
    return resp

@productosBP.route('/obtenerProducto/<codigoBase>', methods=['GET'])
def obtenerProducto(codigoBase):
    conn = Conexion()
    resp = conn.obtenerProducto(codigoBase)
    return resp

@productosBP.route('/obtenerProductosVenta', methods=['GET'])
def obtenerProductosVenta():
    conn = Conexion()
    resp = conn.obtenerProductosVenta()
    return resp

#Editar producto
@productosBP.route('/editarProducto', methods=['PUT'])
def editarProducto():
    data = request.get_json()
    conn = Conexion()
    resp = conn.editarProducto(data)
    return resp

#Eliminar producto
@productosBP.route('/eliminarProducto/<codigoBase>', methods=['DELETE'])
def eliminarProducto(codigoBase):
    conn = Conexion()
    resp = conn.eliminarProducto(codigoBase)
    return resp