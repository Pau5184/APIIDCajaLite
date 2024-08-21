from flask import Blueprint, request
from V1.modelUsuarios import Conexion

usuariosBP = Blueprint('UsuariosBP', __name__)

@usuariosBP.route('/obtenerUsuario', methods=['POST'])
def obtenerUsuario():
    data = request.get_json()
    db_name = request.args.get('db_name')
    if not db_name:
        return {"estatus": "error", "mensaje": "Database name is required"}, 400
    conn = Conexion(db_name)
    resp = conn.obtenerUsuario(data)
    return resp