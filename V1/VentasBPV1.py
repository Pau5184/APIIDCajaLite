from flask import Blueprint, request
from V1.modelVentas import Conexion

ventasBP = Blueprint('VentasBP', __name__)

@ventasBP.route('/registrarVenta', methods=['POST'])
def registrarVenta():
    data = request.get_json()
    db_name = request.args.get('db_name')
    if not db_name:
        return {"estatus": "error", "mensaje": "Database name is required"}, 400
    conn = Conexion(db_name)
    resp = conn.registrarVenta(data)
    return resp

@ventasBP.route('/obtenerVentas', methods=['POST'])
def obtenerVentas():
    data = request.get_json()
    db_name = request.args.get('db_name')
    if not db_name:
        return {"estatus": "error", "mensaje": "Database name is required"}, 400
    conn = Conexion(db_name)
    resp = conn.obtenerVentas(data)
    return resp

@ventasBP.route('/obtenerIdVenta', methods=['POST'])
def obtenerIdVenta():
    data = request.get_json()
    db_name = request.args.get('db_name')
    if not db_name:
        return {"estatus": "error", "mensaje": "Database name is required"}, 400
    conn = Conexion(db_name)
    resp = conn.obtenerIdVenta(data)
    return resp

@ventasBP.route('/obtenerTiquet/<id>', methods=['GET'])
def obtenerTiquet(id):
    db_name = request.args.get('db_name')
    if not db_name:
        return {"estatus": "error", "mensaje": "Database name is required"}, 400
    conn = Conexion(db_name)
    resp = conn.obtenerTiquet(id)
    return resp

@ventasBP.route('/obtenerVenta/<id>', methods=['GET'])
def obtenerVenta(id):
    db_name = request.args.get('db_name')
    if not db_name:
        return {"estatus": "error", "mensaje": "Database name is required"}, 400
    conn = Conexion(db_name)
    resp = conn.obtenerVenta(id)
    return resp

@ventasBP.route('/editarVenta', methods=['PUT'])
def editarVenta():
    data = request.get_json()
    db_name = request.args.get('db_name')
    if not db_name:
        return {"estatus": "error", "mensaje": "Database name is required"}, 400
    conn = Conexion(db_name)
    resp = conn.editarVenta(data)
    return resp