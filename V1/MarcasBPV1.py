from flask import Blueprint, request
from V1.modelMarcas import Conexion

marcasBP = Blueprint('MarcasBP', __name__)

@marcasBP.route('/registrarMarca', methods=['POST'])
def registrarMarca():
    data = request.get_json()
    db_name = request.args.get('db_name')
    if not db_name:
        return {"estatus": "error", "mensaje": "Database name is required"}, 400
    conn = Conexion(db_name)
    resp = conn.registrarMarca(data)
    return resp

@marcasBP.route('/obtenerMarcas', methods=['GET'])
def obtenerMarcas():
    db_name = request.args.get('db_name')
    if not db_name:
        return {"estatus": "error", "mensaje": "Database name is required"}, 400
    conn = Conexion(db_name)
    resp = conn.obtenerMarcas()
    return resp

@marcasBP.route('/editarMarca', methods=['PUT'])
def editarMarca():
    data = request.get_json()
    db_name = request.args.get('db_name')
    if not db_name:
        return {"estatus": "error", "mensaje": "Database name is required"}, 400
    conn = Conexion(db_name)
    resp = conn.editarMarca(data)
    return resp

@marcasBP.route('/eliminarMarca/<id>', methods=['DELETE'])
def eliminarMarca(id):
    db_name = request.args.get('db_name')
    if not db_name:
        return {"estatus": "error", "mensaje": "Database name is required"}, 400
    conn = Conexion(db_name)
    resp = conn.eliminarMarca(id)
    return resp

@marcasBP.route('/obtenerUltimoIdM', methods=['GET'])
def obtenerUltimoIdM():
    db_name = request.args.get('db_name')
    if not db_name:
        return {"estatus": "error", "mensaje": "Database name is required"}, 400
    conn = Conexion(db_name)
    resp = conn.obtenerUltimoIdM()
    return resp