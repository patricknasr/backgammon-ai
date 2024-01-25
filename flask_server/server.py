from flask import Flask, jsonify, request
from flask_server.src.utilities import process_integer

app = Flask(__name__)

@app.route("/")
def home():
    return 'Hello, Backgammon!'

@app.route('/process-integer', methods=['POST'])
def handle_integer():
    data = request.get_json()
    input_integer = int(data.get('integer'))
    operation = data.get('operation')
    result = process_integer(input_integer, operation)
    return jsonify({'result': result})

if __name__ == "__main__":
    app.run(debug=True)
