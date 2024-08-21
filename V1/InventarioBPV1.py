from flask import Blueprint, request
from V1.modelInventario import Conexion

inventarioBP = Blueprint('InventarioBP', __name__)

@inventarioBP.route('/registrarInventario', methods=['POST'])
def registrarInventario():
    data = request.get_json()
    db_name = request.args.get('db_name')
    if not db_name:
        return {"estatus": "error", "mensaje": "Database name is required"}, 400
    conn = Conexion(db_name)
    resp = conn.registrarInventario(data)
    return resp

@inventarioBP.route('/obtenerInventarios', methods=['POST'])
def obtenerInventarios():
    data = request.get_json()
    db_name = request.args.get('db_name')
    if not db_name:
        return {"estatus": "error", "mensaje": "Database name is required"}, 400
    conn = Conexion(db_name)
    resp = conn.obtenerInventarios(data)
    return resp

@inventarioBP.route('/obtenerInventario/<id>', methods=['GET'])
def obtenerInventario(id):
    db_name = request.args.get('db_name')
    if not db_name:
        return {"estatus": "error", "mensaje": "Database name is required"}, 400
    conn = Conexion(db_name)
    resp = conn.obtenerInventario(id)
    return resp