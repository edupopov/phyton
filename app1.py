from flask import Flask, jsonify

app1 = Flask(__name__)

@app1.route('/')
def home():
    return "Hello, Flask!"

items = []

@app1.route('/items', methods=['GET'])
def get_items():
    return jsonify(items)

if __name__ == '__main__':
    app1.run(debug=True)
