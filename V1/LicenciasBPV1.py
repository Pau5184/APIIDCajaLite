from flask import Blueprint, request
from V1.modelLicencias import Conexion

licenciasBP = Blueprint('LicenciasBP',__name__)

@licenciasBP.route('/registrarLicencia', methods=['POST'])
def registrarLicencia():
    data = request.get_json()
    conn = Conexion()
    resp = conn.registrarLicencia(data)
    return resp

#Validate license
@licenciasBP.route('/validarLicencia', methods=['POST'])
def validarLicencia():
    data = request.get_json()
    conn = Conexion()
    resp = conn.validarLicencia(data)
    return resp

#Get licenses
@licenciasBP.route('/obtenerLicencias', methods=['GET'])
def obtenerLicencias():
    conn = Conexion()
    resp = conn.obtenerLicencias()
    return resp

#Activate license
@licenciasBP.route('/activarLicencia', methods=['POST'])
def activarLicencia():
    data = request.get_json()
    conn = Conexion()
    resp = conn.activarLicencia(data)
    return resp