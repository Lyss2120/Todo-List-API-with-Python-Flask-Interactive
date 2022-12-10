from flask import Flask, jsonify
from flask import request
import json
app = Flask(__name__)


todos = [ { "label": "My first task", "done": False } ]

@app.route('/todos', methods=['GET'])
def hello_world():
    json_text = jsonify(todos)
    return json_text

@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.data
    decoded_object = json.loads(request_body)
    todos.append(decoded_object)
    print("Incoming request with the following body", request_body)
    return jsonify(todos)

# @app.route('/todos/<int:position>', methods=['DELETE'])
# def delete_todo(position):
#     # request_body = request.data
#     # decoded_object = json.loads(request_body)
#     # todos.pop(position)
#     print("This is the position to delete: ", position)
#     return jsonify(todos)

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    parametros = request.get_json()
    todos.pop(position)
    print("This is the position to delete: ",position)
    return jsonify(todos)
    # borra todos los que agregue con POST solo deja el primero 
    #por defecto







if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
