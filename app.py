from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/saludo', methods=['POST'])
def saludar():
    nombre = request.json.get('nombre')
    if nombre:
        mensaje = f'Hola, {nombre}! ¡Bienvenido a la API!'
        return jsonify({'mensaje': mensaje})
    else:
        return jsonify({'error': 'Nombre no proporcionado'}), 400
    
@app.route('/saludo', methods=['GET'])
def saludar():
    return '¡Hola! Esta es mi API de saludo.'

if __name__ == '__main__':
    app.run(debug=True)
