from flask import Flask, jsonify, request
import requests

app = Flask(__name__)


servers = {
    'shard1': 'http://shard1:5000',
    'shard2': 'http://shard2:5000',
    'shard3': 'http://shard3:5000',
}

@app.route('/user/<shard_id>/<user_id>', methods=['GET'])
def redirect_to_shard(shard_id, user_id):
    
    if shard_id not in servers:
        return jsonify({'error': f'Shard {shard_id} not found'}), 404

  
    server_url = servers[shard_id]

    try:
      
        destination_url = f'{server_url}/user/{shard_id}/{user_id}'
        response = requests.get(destination_url)

    
        return jsonify(response.json()), response.status_code

    except requests.exceptions.RequestException as e:
       
        return jsonify({'error': f'Error making HTTP request: {e}'}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)  # Asegúrate de que el puerto aquí coincida con el puerto expuesto en docker-compose para el embajador
