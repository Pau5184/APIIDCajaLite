from flask import Blueprint, request
from V1.modelEmpresa import Conexion

empresaBP = Blueprint('EmpresaBP', __name__)

@empresaBP.route('/obtenerEmpresa', methods=['GET'])
def obtenerEmpresa():
    conn = Conexion()
    resp = conn.obtenerEmpresa()
    return resp

@empresaBP.route('/editarEmpresa', methods=['PUT'])
def editarEmpresa():
    data = request.get_json()
    conn = Conexion()
    resp = conn.editarEmpresa(data)
    return resp