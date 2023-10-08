from flask import Flask, request, jsonify
from flask_cors import CORS  # Import CORS from flask_cors

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return 'Hello, World!'

#600 code for success

@app.route('/getUser/<username>')
def about(username):
    user = {
        "name": username,
        "age": 20
    }

    extra = request.args.get('extra')
    if extra:
        user["extra"] = extra

    return jsonify(user), 200

#http://127.0.0.1:5000/getUser/a?extra=info

@app.route('/postUser', methods=['POST'])
def postUser():
    if request.method == 'POST':
        print("is post")

    data = request.get_json()
    #add to database
    print("Data: ", data)
    return jsonify(data), 201


if __name__ == '__main__':
    app.run(debug=True)