import logging
from flask import Flask, request

# Configurar el módulo de logging
logging.basicConfig(level=logging.INFO)

app = Flask(__name__)

@app.route('/log', methods=['POST'])
def log_event():
    data = request.get_json()
    message = data['message']
    # Registrar el mensaje usando logging en lugar de print()
    logging.info(f"Logged event: {message}")
    return {"status": "success"}, 200

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001)
