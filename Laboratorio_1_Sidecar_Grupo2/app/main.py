import logging
from flask import Flask, request, jsonify
import requests

# Configurar el módulo de logging
logging.basicConfig(level=logging.INFO)

app = Flask(__name__)

class Main:
    def process_message(self, message):
        logging.info(f"Processing message: {message}")
        # Asumiendo que el sidecar se ejecuta en el host 'logger' y el puerto 5001
        response = requests.post("http://logger:5001/log", json={"message": message})
        if response.status_code == 200:
            return "Event logged successfully"
        else:
            return "Failed to log event"

@app.route('/process', methods=['POST'])
def process():
    data = request.get_json()
    message = data['message']
    response = Main().process_message(message)
    # Devolver la respuesta como JSON
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
