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