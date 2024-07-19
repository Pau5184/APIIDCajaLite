from flask import Blueprint, request
from V1.modelInventario import Conexion

inventarioBP = Blueprint('InventarioBP', __name__)

@inventarioBP.route('/registrarInventario', methods=['POST'])
def registrarInventario():
    data = request.get_json()
    conn = Conexion()
    resp = conn.registrarInventario(data)
    return resp

@inventarioBP.route('/obtenerInventarios', methods=['POST'])
def obtenerInventarios():
    data = request.get_json()
    conn = Conexion()
    resp = conn.obtenerInventarios(data)
    return resp

@inventarioBP.route('/obtenerInventario/<id>', methods=['GET'])
def obtenerInventario(id):
    conn = Conexion()
    resp = conn.obtenerInventario(id)
    return resp