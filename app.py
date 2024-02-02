from flask import Flask
from V1.ProductosBPV1 import productosBP
from flask_cors import CORS

app=Flask(__name__)
##CORS(app)
app.register_blueprint(productosBP)

@app.route('/',methods=['GET'])
def init():
    return "Escuchando el Servicio REST de ID Caja Lite"

if __name__=='__main__':
    app.run(debug=True)##, host='192.168.1.66', port=5000)