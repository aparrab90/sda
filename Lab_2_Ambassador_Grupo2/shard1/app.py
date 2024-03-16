from flask import Flask, jsonify, json

app = Flask(__name__)


with open('datashard1.json') as json_file:
    users_data = json.load(json_file)

@app.route('/user/<shard_id>/<user_id>')
def get_user(shard_id, user_id):

    if shard_id not in users_data:
        return jsonify({'error': f'Shard {shard_id} not found'}), 404

    shard = users_data[shard_id]


    if user_id not in shard:
        return jsonify({'error': f'User {user_id} not found in shard {shard_id}'}), 404

    user = shard[user_id]
    return jsonify(user)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
