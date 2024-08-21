from flask import Blueprint, request
from V1.modelUnidades import Conexion

unidadesBP = Blueprint('UnidadesBP', __name__)

@unidadesBP.route('/registrarUnidad', methods=['POST'])
def registrar_unidad():
    data = request.get_json()
    db_name = request.args.get('db_name')
    if not db_name:
        return {"estatus": "error", "mensaje": "Database name is required"}, 400
    conn = Conexion(db_name)
    resp = conn.registrarUnidad(data)
    return resp

@unidadesBP.route('/obtenerUnidades', methods=['GET'])
def obtener_unidades():
    db_name = request.args.get('db_name')
    if not db_name:
        return {"estatus": "error", "mensaje": "Database name is required"}, 400
    conn = Conexion(db_name)
    resp = conn.obtenerUnidades()
    return resp

@unidadesBP.route('/editarUnidad', methods=['PUT'])
def editar_unidad():
    data = request.get_json()
    db_name = request.args.get('db_name')
    if not db_name:
        return {"estatus": "error", "mensaje": "Database name is required"}, 400
    conn = Conexion(db_name)
    resp = conn.editarUnidad(data)
    return resp

@unidadesBP.route('/eliminarUnidad/<idUnidad>', methods=['DELETE'])
def eliminar_unidad(idUnidad):
    db_name = request.args.get('db_name')
    if not db_name:
        return {"estatus": "error", "mensaje": "Database name is required"}, 400
    conn = Conexion(db_name)
    resp = conn.eliminarUnidad(idUnidad)
    return resp

@unidadesBP.route('/obtenerUltimoIdU', methods=['GET'])
def obtenerUltimoIdU():
    db_name = request.args.get('db_name')
    if not db_name:
        return {"estatus": "error", "mensaje": "Database name is required"}, 400
    conn = Conexion(db_name)
    resp = conn.obtenerUltimoIdU()
    return resp