from flask import Blueprint, request
from V1.modelLineas import Conexion

lineasBP = Blueprint('LineasBP', __name__)

@lineasBP.route('/registrarLinea', methods=['POST'])
def registrar_linea():
    data = request.get_json()
    db_name = request.args.get('db_name')
    if not db_name:
        return {"estatus": "error", "mensaje": "Database name is required"}, 400
    conn = Conexion(db_name)
    resp = conn.registrarLinea(data)
    return resp

@lineasBP.route('/obtenerLineas', methods=['GET'])
def obtener_lineas():
    db_name = request.args.get('db_name')
    if not db_name:
        return {"estatus": "error", "mensaje": "Database name is required"}, 400
    conn = Conexion(db_name)
    resp = conn.obtenerLineas()
    return resp

@lineasBP.route('/editarLinea', methods=['PUT'])
def editar_linea():
    data = request.get_json()
    db_name = request.args.get('db_name')
    if not db_name:
        return {"estatus": "error", "mensaje": "Database name is required"}, 400
    conn = Conexion(db_name)
    resp = conn.editarLinea(data)
    return resp

@lineasBP.route('/eliminarLinea/<idLinea>', methods=['DELETE'])
def eliminar_linea(idLinea):
    db_name = request.args.get('db_name')
    if not db_name:
        return {"estatus": "error", "mensaje": "Database name is required"}, 400
    conn = Conexion(db_name)
    resp = conn.eliminarLinea(idLinea)
    return resp

@lineasBP.route('/obtenerUltimoIdL', methods=['GET'])
def obtenerUltimoIdL():
    db_name = request.args.get('db_name')
    if not db_name:
        return {"estatus": "error", "mensaje": "Database name is required"}, 400
    conn = Conexion(db_name)
    resp = conn.obtenerUltimoIdL()
    return resp