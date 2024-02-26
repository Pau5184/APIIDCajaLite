from flask import Blueprint, request
from V1.modelUsuarios import Conexion

usuariosBP = Blueprint('UsuariosBP', __name__)

@usuariosBP.route('/obtenerUsuario', methods=['POST'])
def obtenerUsuario():
    data = request.get_json()
    conn = Conexion()
    resp = conn.obtenerUsuario(data)
    return resp