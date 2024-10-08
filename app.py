from flask import Flask
from V1.ProductosBPV1 import productosBP
from V1.ClientesBPV1 import clientesBP
from V1.MarcasBPV1 import marcasBP
from V1.LineasBPV1 import lineasBP
from V1.VentasBPV1 import ventasBP
from V1.UsuariosBPV1 import usuariosBP
from V1.InventarioBPV1 import inventarioBP
from V1.UnidadesBPV1 import unidadesBP
from V1.EmpresaBPV1 import empresaBP
from V1.LicenciasBPV1 import licenciasBP
from flask_cors import CORS

app=Flask(__name__)
CORS(app)
app.register_blueprint(productosBP)
app.register_blueprint(clientesBP)
app.register_blueprint(marcasBP)
app.register_blueprint(lineasBP)
app.register_blueprint(ventasBP)
app.register_blueprint(usuariosBP)
app.register_blueprint(inventarioBP)
app.register_blueprint(unidadesBP)
app.register_blueprint(empresaBP)
app.register_blueprint(licenciasBP)

@app.route('/',methods=['GET'])
def init():
    return "Escuchando el Servicio REST de ID Caja Lite"

if __name__=='__main__':
    #app.run(debug=True, host='10.0.4.23', port=5000)
    app.run(host='0.0.0.0', port=8080)