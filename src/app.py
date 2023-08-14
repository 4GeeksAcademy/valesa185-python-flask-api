from flask import Flask
from flask import Flask, jsonify
from flask import request

app = Flask(__name__)

todos = [
    {
        "done": True,
        "label": "Sample Todo 1"
    },
    {
        "done": True,
        "label": "Sample Todo 2"
    }
]

"""Metodo GET"""
@app.route('/todos', methods=['GET'])
def hello_world():
    json_text = jsonify(todos)
    return json_text

"""Metodo POST"""
@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.get_json(force=True)
    print("Incoming request with the following body", request_body)  
   
    todos.append(request_body)  
    return jsonify(todos)  

"""Metodo DELETE"""
@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    print("This is the position to delete: ",position)

    todos.pop(position)  
    return jsonify(todos)  


# These two lines should always be at the end of your app.py file.
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)