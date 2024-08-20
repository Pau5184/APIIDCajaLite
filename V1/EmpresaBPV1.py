from flask import Blueprint, request
from V1.modelEmpresa import Conexion

empresaBP = Blueprint('EmpresaBP', __name__)

@empresaBP.route('/obtenerEmpresa', methods=['GET'])
def obtenerEmpresa():
    db_name = request.args.get('db_name')
    if not db_name:
        return {"estatus": "error", "mensaje": "Database name is required"}, 400
    conn = Conexion(db_name)
    resp = conn.obtenerEmpresa()
    return resp

@empresaBP.route('/editarEmpresa', methods=['PUT'])
def editarEmpresa():
    data = request.get_json()
    db_name = request.args.get('db_name')
    if not db_name:
        return {"estatus": "error", "mensaje": "Database name is required"}, 400
    conn = Conexion(db_name)
    resp = conn.editarEmpresa(data)
    return resp