from flask import Flask, jsonify, request
from nameko.standalone.rpc import ClusterRpcProxy

app = Flask(__name__)

@app.route('/users')
def get_all_users():
    with ClusterRpcProxy({'AMQP_URI': "pyamqp://guest:guest@localhost"}) as rpc:
        user_list = rpc.user_service.get_all_users()
        return jsonify(user_list)
    
@app.route('/users', methods=['POST'])
def create_user():
    with ClusterRpcProxy({'AMQP_URI': "pyamqp://guest:guest@localhost"}) as rpc:
        data = request.get_json()
        name = data.get('name')
        email = data.get('email')
        password = data.get('password')

        if not all([name, email, password]):
            return jsonify({'error': 'missing required fields'}), 400

        user = rpc.user_service.create_user(name, email, password)
        return jsonify(user), 201


@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    data = request.get_json()
    name = data.get('name')
    email = data.get('email')
    password = data.get('password')

    with ClusterRpcProxy({'AMQP_URI': "pyamqp://guest:guest@localhost"}) as rpc:
        updated_user = rpc.user_service.update_user(user_id=user_id, name=name, email=email, password=password)

    if 'error' in updated_user:
        return jsonify(updated_user), 404

    return jsonify(updated_user), 200
if __name__ == '__main__':
    app.run(debug=True)
