from flask import Blueprint, request
from V1.modelMarcas import Conexion

marcasBP = Blueprint('MarcasBP', __name__)

@marcasBP.route('/registrarMarca', methods=['POST'])
def registrarMarca():
    data = request.get_json()
    conn = Conexion()
    resp = conn.registrarMarca(data)
    return resp

@marcasBP.route('/obtenerMarcas', methods=['GET'])
def obtenerMarcas():
    conn = Conexion()
    resp = conn.obtenerMarcas()
    return resp

@marcasBP.route('/editarMarca', methods=['PUT'])
def editarMarca():
    data = request.get_json()
    conn = Conexion()
    resp = conn.editarMarca(data)
    return resp

@marcasBP.route('/eliminarMarca/<id>', methods=['DELETE'])
def eliminarMarca(id):
    conn = Conexion()
    resp = conn.eliminarMarca(id)
    return resp

@marcasBP.route('/obtenerUltimoIdM', methods=['GET'])
def obtenerUltimoIdM():
    conn = Conexion()
    resp = conn.obtenerUltimoIdM()
    return resp