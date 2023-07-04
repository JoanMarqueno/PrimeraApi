from flask import Flask
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
api = Api(app)

# Creamos una lista para almacenar las tareas
tasks = []

# Definimos el analizador de argumentos para las solicitudes POST y PUT
parser = reqparse.RequestParser()
parser.add_argument('task', type=str, required=True, help='El campo task es requerido.')

# Definimos una clase para manejar las solicitudes a /tasks
class TasksResource(Resource):
    def get(self):
        return tasks

    def post(self):
        args = parser.parse_args()
        task = args['task']
        tasks.append(task)
        return {'message': 'Tarea agregada correctamente'}, 201

# Definimos una clase para manejar las solicitudes a /tasks/<int:id>
class TaskResource(Resource):
    def get(self, id):
        if id >= len(tasks) or id < 0:
            return {'error': 'Tarea no encontrada'}, 404
        return tasks[id]

    def put(self, id):
        if id >= len(tasks) or id < 0:
            return {'error': 'Tarea no encontrada'}, 404
        args = parser.parse_args()
        task = args['task']
        tasks[id] = task
        return {'message': 'Tarea actualizada correctamente'}

    def delete(self, id):
        if id >= len(tasks) or id < 0:
            return {'error': 'Tarea no encontrada'}, 404
        task = tasks.pop(id)
        return {'message': 'Tarea eliminada correctamente'}

# Agregamos las rutas a la API
api.add_resource(TasksResource, '/tasks')
api.add_resource(TaskResource, '/tasks/<int:id>')

if __name__ == '__main__':
    app.run(debug=True)
