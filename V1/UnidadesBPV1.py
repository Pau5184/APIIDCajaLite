from flask import Blueprint, request
from V1.modelUnidades import Conexion

unidadesBP = Blueprint('UnidadesBP', __name__)

@unidadesBP.route('/registrarUnidad', methods=['POST'])
def registrar_unidad():
    data = request.get_json()
    conn = Conexion()
    resp = conn.registrarUnidad(data)
    return resp

@unidadesBP.route('/obtenerUnidades', methods=['GET'])
def obtener_unidades():
    conn = Conexion()
    resp = conn.obtenerUnidades()
    return resp

@unidadesBP.route('/editarUnidad', methods=['PUT'])
def editar_unidad():
    data = request.get_json()
    conn = Conexion()
    resp = conn.editarUnidad(data)
    return resp

@unidadesBP.route('/eliminarUnidad/<idUnidad>', methods=['DELETE'])
def eliminar_unidad(idUnidad):
    conn = Conexion()
    resp = conn.eliminarUnidad(idUnidad)
    return resp

@unidadesBP.route('/obtenerUltimoIdU', methods=['GET'])
def obtenerUltimoIdU():
    conn = Conexion()
    resp = conn.obtenerUltimoIdU()
    return resp