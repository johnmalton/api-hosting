from flask import Flask, request, jsonify

app = Flask(__name__)

users_1 = []
users_2 = []

# @app.route('/api/users-1', methods=['POST'])
@app.post('/api/users-1')
def create_user_1():
    data = request.json
    name = data.get('name')
    email = data.get('email')
    new_user = {'name': name, 'email': email}
    users_1.append(new_user)
    return jsonify(users_1), 202


# @app.route('/api/users-2', methods=['POST'])
@app.post("/api/users-2")
def create_user_2():
    new_user = request.get_json()
    users_2.append(new_user)
    # print(users_2)
    return jsonify(users_2), 201

@app.get('/api/all-users')
def get_users():
    global users_1, users_2
    sent = f"Users 1: {users_1}, Users 2: {users_2}"
    return jsonify(sent), 200


