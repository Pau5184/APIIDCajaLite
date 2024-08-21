from flask import Blueprint, request
from V1.modelClientes import Conexion

clientesBP = Blueprint('ClientesBP', __name__)

@clientesBP.route('/registrarCliente', methods=['POST'])
def registrarCliente():
    data = request.get_json()
    db_name = request.args.get('db_name')
    if not db_name:
        return {"estatus": "error", "mensaje": "Database name is required"}, 400
    conn = Conexion(db_name)
    resp = conn.registrarCliente(data)
    return resp

@clientesBP.route('/obtenerClientes', methods=['GET'])
def obtenerClientes():
    db_name = request.args.get('db_name')
    if not db_name:
        return {"estatus": "error", "mensaje": "Database name is required"}, 400
    conn = Conexion(db_name)
    resp = conn.obtenerClientes()
    return resp

@clientesBP.route('/obtenerCliente/<id>', methods=['GET'])
def obtenerCliente(id):
    db_name = request.args.get('db_name')
    if not db_name:
        return {"estatus": "error", "mensaje": "Database name is required"}, 400
    conn = Conexion(db_name)
    resp = conn.obtenerCliente(id)
    return resp

@clientesBP.route('/obtenerClienteNombre', methods=['POST'])
def obtenerClienteNombre():
    data = request.get_json()
    db_name = request.args.get('db_name')
    if not db_name:
        return {"estatus": "error", "mensaje": "Database name is required"}, 400
    conn = Conexion(db_name)
    resp = conn.obtenerClienteNombre(data)
    return resp

@clientesBP.route('/obtenerClientesVenta', methods=['GET'])
def obtenerClientesVenta():
    db_name = request.args.get('db_name')
    if not db_name:
        return {"estatus": "error", "mensaje": "Database name is required"}, 400
    conn = Conexion(db_name)
    resp = conn.obtenerClientesVenta()
    return resp

@clientesBP.route('/editarCliente', methods=['PUT'])
def editarCliente():
    data = request.get_json()
    db_name = request.args.get('db_name')
    if not db_name:
        return {"estatus": "error", "mensaje": "Database name is required"}, 400
    conn = Conexion(db_name)
    resp = conn.editarCliente(data)
    return resp

@clientesBP.route('/eliminarCliente/<id>', methods=['DELETE'])
def eliminarCliente(id):
    db_name = request.args.get('db_name')
    if not db_name:
        return {"estatus": "error", "mensaje": "Database name is required"}, 400
    conn = Conexion(db_name)
    resp = conn.eliminarCliente(id)
    return resp