from flask import Flask, jsonify, request
app = Flask(__name__)

todos = [
    { "label": "Cocinar", "done": False },
    { "label": "Beber agua", "done": True }
]
@app.route('/todos', methods=['GET'])
def hello_world():
       # You can convert that variable into a json string like this
    json_text = jsonify(todos)
    return json_text

@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.get_json(force=True)
    print("Incoming request with the following body", request_body)
    todos.append(request_body) 
    return jsonify(todos)

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    if position < 0 or position >= len(todos):
        return jsonify({"error": "Index out of range"}), 404

    todos.pop(position)
    return jsonify(todos), 200

# These two lines should always be at the end of your app.py file
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3245, debug=True)