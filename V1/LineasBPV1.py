from flask import Blueprint, request
from V1.modelLineas import Conexion

lineasBP = Blueprint('LineasBP', __name__)

@lineasBP.route('/registrarLinea', methods=['POST'])
def registrar_linea():
    data = request.get_json()
    conn = Conexion()
    resp = conn.registrarLinea(data)
    return resp

@lineasBP.route('/obtenerLineas', methods=['GET'])
def obtener_lineas():
    conn = Conexion()
    resp = conn.obtenerLineas()
    return resp

@lineasBP.route('/editarLinea', methods=['PUT'])
def editar_linea():
    data = request.get_json()
    conn = Conexion()
    resp = conn.editarLinea(data)
    return resp

@lineasBP.route('/eliminarLinea/<idLinea>', methods=['DELETE'])
def eliminar_linea(idLinea):
    conn = Conexion()
    resp = conn.eliminarLinea(idLinea)
    return resp

@lineasBP.route('/obtenerUltimoIdL', methods=['GET'])
def obtenerUltimoIdL():
    conn = Conexion()
    resp = conn.obtenerUltimoIdL()
    return resp