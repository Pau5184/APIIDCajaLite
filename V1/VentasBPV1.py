from flask import Blueprint, request
from V1.modelVentas import Conexion

ventasBP = Blueprint('VentasBP', __name__)

@ventasBP.route('/registrarVenta', methods=['POST'])
def registrarVenta():
    data = request.get_json()
    conn = Conexion()
    resp = conn.registrarVenta(data)
    return resp

@ventasBP.route('/obtenerVentas', methods=['POST'])
def obtenerVentas():
    data = request.get_json()
    conn = Conexion()
    resp = conn.obtenerVentas(data)
    return resp

@ventasBP.route('/obtenerIdVenta', methods=['POST'])
def obtenerIdVenta():
    data = request.get_json()
    conn = Conexion()
    resp = conn.obtenerIdVenta(data)
    return resp

@ventasBP.route('/obtenerTiquet/<id>', methods=['GET'])
def obtenerTiquet(id):
    conn = Conexion()
    resp = conn.obtenerTiquet(id)
    return resp

@ventasBP.route('/editarVenta', methods=['PUT'])
def editarVenta():
    data = request.get_json()
    conn = Conexion()
    resp = conn.editarVenta(data)
    return resp