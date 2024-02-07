from flask import Blueprint, request
from V1.modelClientes import Conexion

clientesBP = Blueprint('ClientesBP', __name__)

@clientesBP.route('/registrarCliente', methods=['POST'])
def registrarCliente():
    data = request.get_json()
    conn = Conexion()
    resp = conn.registrarCliente(data)
    return resp

@clientesBP.route('/obtenerClientes', methods=['GET'])
def obtenerClientes():
    conn = Conexion()
    resp = conn.obtenerClientes()
    return resp

@clientesBP.route('/obtenerCliente/<id>', methods=['GET'])
def obtenerCliente(id):
    conn = Conexion()
    resp = conn.obtenerCliente(id)
    return resp

@clientesBP.route('/obtenerClientesVenta', methods=['GET'])
def obtenerClientesVenta():
    conn = Conexion()
    resp = conn.obtenerClientesVenta()
    return resp

@clientesBP.route('/editarCliente', methods=['PUT'])
def editarCliente():
    data = request.get_json()
    conn = Conexion()
    resp = conn.editarCliente(data)
    return resp

@clientesBP.route('/eliminarCliente/<id>', methods=['DELETE'])
def eliminarCliente(id):
    conn = Conexion()
    resp = conn.eliminarCliente(id)
    return resp