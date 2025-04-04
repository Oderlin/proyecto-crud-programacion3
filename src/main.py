from flask import Flask, jsonify, request

app = Flask(__name__)
items = []

@app.route('/items', methods=['GET'])
def get_items():
    return jsonify(items)

@app.route('/items', methods=['POST'])
def add_item():
    item = request.json
    items.append(item)
    return jsonify(item), 201

if __name__ == '__main__':
    app.run(debug=True)
